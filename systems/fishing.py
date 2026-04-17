from sprites.fish import Fish
from sprites.player import Player 
from systems.inventory import Inventory
import random 
class Fishing:
    def __init__( self, fish_list: list[Fish], player: Player, inv: Inventory ):
        self.fish_list = fish_list
        self.player = player
        self.inv = inv
    def select_fish( self ):
        idx = random.randint( 0, len( self.fish_list ) - 1 )
        return self.fish_list[ idx ]

        