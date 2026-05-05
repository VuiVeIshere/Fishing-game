import json
from sprites.player import Player
from sprites.fish import Fish
from systems.inventory import Inventory
import hashlib 
import os
class Save:
    """
    Xử lý việc lưu và tải dữ liệu người chơi.

    Dữ liệu bao gồm:
    - Thông tin player
    - Inventory
    - Tiến trình game

    Attributes:
        player (Player): Người chơi
        file_path (str): Đường dẫn file lưu dữ liệu
    """
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
        """
        Lưu dữ liệu người chơi vào file.

        Ghi lại:
        - Thông tin player
        - Inventory
        - Trạng thái game
        """
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
        """
        Tải dữ liệu người chơi từ file.

        Returns:
            Player: Đối tượng player đã được khôi phục
        """
        data = self.load_all()
        password_hash = hashlib.sha256( self.password.encode() ).hexdigest()
        state = data["players"].get( name )
        if state is None:
            return None
        if state["password"] != password_hash:
            print( "Sai mật khẩu!" )
            return 0
        player = Player.from_dict( state["player"] )
        fish_list = [ Fish.from_dict( fish ) for fish in state["inv"] ]
        return player, fish_list    
    