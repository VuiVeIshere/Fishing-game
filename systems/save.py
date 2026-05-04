import json
from sprites.player import Player
from sprites.fish import Fish
from systems.inventory import Inventory
import hashlib 
import os
class Save:
    def __init__( self, player: Player, inv: Inventory, password ):
        self.player = player
        self.inv = inv
        self.password = password
    def load_all( self ):
        if not os.path.exists( "save.json" ):
            return {"players": {}}
        with open( "save.json", "r") as f:
            return json.load(f)
        
    def save_all( self, data ):
        with open("save.tmp", "w") as f:
            json.dump(data, f, indent=4)
        os.replace("save.tmp", "save.json" )  

    def save_player( self ):
        data = self.load_all()     
        password_hash = hashlib.sha256( self.password.encode() ).hexdigest() 
        state = {
            "password": password_hash,
            "player": self.player.to_dict(),
            "inv": [ fish.to_dict() for fish in self.inv.fish_list ]
        }          
        data["players"][self.player.player_name] = state  
        self.save_all( data )     

    def load_player( self, name ):
        data = self.load_all()
        password_hash = hashlib.sha256( self.password.encode() ).hexdigest()
        state = data["players"].get( name )
        if state is None:
            return None
        if state["password"] != password_hash:
            return None
        player = Player.from_dict(state["player"])
        fish_list = [ Fish.from_dict( fish ) for fish in state["inv"] ]
        return player, fish_list    
    