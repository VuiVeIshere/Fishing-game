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
    def get_adjusted_rates( self, dict_fish, rod ): #GPT help
        adjusted = {}

        for fish, data in dict_fish.items():
            rarity = data[ "rarity" ]
            base_rate = data[ "rate" ]

            bonus = rod[ "bonus" ].get(rarity, 1.0)
            adjusted[ fish ] = base_rate * bonus

        return adjusted
    def select_fish( self ):
        x = self.get_adjusted_rates( self.data.dict_fish, self.player.rod_bonus )
        fish_name = random.choices( list( x.keys() ), weights = list( x.values() ), k = 1  )[0]
        fish = self.data.dict_fish[ fish_name ]
        weight_approx = fish[ "weight" ]
        if weight_approx > 100:
            fish_weight = round( random.uniform( weight_approx - 50, weight_approx + 50 ), 2 )
        else:
            fish_weight = round( random.uniform( weight_approx - 0.5, weight_approx + 0.5 ), 2 )
        return Fish( fish_name, fish[ "rarity" ], fish_weight ) 
 
        