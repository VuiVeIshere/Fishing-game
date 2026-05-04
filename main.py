from sprites.fish import Fish
from sprites.player import Player
from systems.fishing import Fishing
from systems.inventory import Inventory
from game.game import Game
from systems.hash_utils import Hash
from data.data import Data
from sprites.rod import Rod
from systems.shopping import Shop
from systems.save import Save


def main():
    name = input( "Nhập tên người chơi: " )
    password = input( "Nhập mật khẩu: " )
    temp_player = Player( name )
    temp_inv = Inventory( temp_player )
    save = Save( temp_player, temp_inv, password )
    result = save.load_player( name )
    if result is None:
        print( "Đã tạo người chơi mới" )
        player, inv = temp_player, temp_inv
        fish_list = []
    else:
        player, fish_list = result
        inv = Inventory( player, fish_list )
        print(f"Welcome back {player.player_name}!")
    save = Save( player, inv, password )
    game = Game( player, save, fish_list )
    game.play()
    
if __name__ == "__main__":
    main()