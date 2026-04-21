from sprites.fish import Fish
from sprites.player import Player 
from systems.inventory import Inventory
from data.data import Data
import random 
class Fishing:
    def __init__( self, player: Player, inv: Inventory ):
        self.player = player
        self.inv = inv
        self.data = Data()
    def select_fish( self ):
        fish_name = random.choice( list( self.data.dict_fish ) )
        fish_rarity = self.data.dict_fish[ fish_name ]
        weight_approx = self.data.fish_weights[ fish_name ]
        if weight_approx > 100:
            fish_weight = round( random.uniform( weight_approx - 50, weight_approx + 50 ), 2 )
        else:
            fish_weight = round( random.uniform( weight_approx - 0.5, weight_approx + 0.5 ), 2 )
        return Fish( fish_name, fish_rarity, fish_weight ) 
 
        