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
from systems.leaderboard import Leaderboard

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
        print(f"Chào mừng {player.player_name} quay trở lại !")
    save = Save( player, inv, password )
    players = save.load_all()
    leaderboard = Leaderboard()
    for username, state in players["players"].items():
        p = state["player"]
        leaderboard.update( username, p["coins"], p["level"] )
   
    game = Game( player, save, fish_list, leaderboard )
    game.play()
    
if __name__ == "__main__":
    main()