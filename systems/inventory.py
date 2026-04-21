from sprites.fish import Fish
from sprites.player import Player 
from systems.hash_utils import Hash
from data.data import Data
class Inventory:
    def __init__( self, player: Player ):
        self.player = player
        self.fish_list = []
        self.hash = Hash( 100 )
    def add_fish( self, fish: Fish ):
        self.fish_list.append( fish )
        hash_val = self.hash.get_hash_index( fish.name )
        self.hash.insert( fish.name )
        if hash_val not in self.player.hash_to_name:
            self.player.hash_to_name[ hash_val ] = fish.name
        if hash_val in self.player.inventory:
            self.player.inventory[ hash_val ] += 1
        else:
            self.player.inventory[ hash_val ] = 1
    def show( self ):
        print( "====Inventory====")
        if not self.player.inventory:
            print( "Túi đồ của bạn không có gì :( ")
        else:
            for hash_val, quantity in self.player.inventory.items():
                print( self.player.hash_to_name[ hash_val ], " - ", quantity, " con." )
    def sell_fish( self, fish_name = "", quantity = 0, all = 0 ):
        fish_name = fish_name.lower().capitalize()
        money = 0
        if all:
            for fish in self.fish_list:
                money += fish.value
            self.player.inventory.clear()
            self.fish_list.clear()
        else:
            hash_val = self.hash.get_hash_index( fish_name )
            if hash_val not in self.player.inventory:
                print( f"Túi đồ của bạn không có cá {fish_name}!" )
            elif quantity <= 0 or quantity > self.player.inventory[ hash_val ]:
                print( f"Số lượng cá muốn bán không hợp lệ!" )
            else:
                for i in range ( quantity ):
                    for fish in self.fish_list:
                        if fish.name == fish_name:
                            money += fish.value
                            self.fish_list.remove( fish )
                            break
            self.player.coins += money
            print( f"Bạn đã bán tất cả cá trong kho và được {money} xu!" )
            print( f"Bạn hiện đang có {self.player.coins} xu!" )