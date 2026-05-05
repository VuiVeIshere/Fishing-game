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
import re 
def is_valid_format( username ):
    """
    Kiểm tra định dạng hợp lệ của tên người chơi.

    Chỉ cho phép:
    - Chữ cái (a-z, A-Z)
    - Số (0-9)
    - Dấu gạch dưới (_)

    Args:
        username (str): Tên người chơi

    Returns:
        Match | None: Đối tượng match nếu hợp lệ, ngược lại là None
    """
    return re.match( r'^[a-zA-Z0-9_]+$', username )
def main():
    """
    Hàm chính của chương trình.

    Thực hiện:
    - Nhập và kiểm tra tên người chơi
    - Đăng nhập hoặc tạo người chơi mới
    - Tải dữ liệu từ hệ thống lưu trữ
    - Khởi tạo inventory và leaderboard
    - Khởi chạy game

    Luồng hoạt động:
    1. Người chơi nhập username và password
    2. Kiểm tra username hợp lệ
    3. Load dữ liệu nếu đã tồn tại, ngược lại tạo mới
    4. Khởi tạo leaderboard từ dữ liệu tất cả người chơi
    5. Tạo đối tượng Game và bắt đầu vòng lặp game
    """
    result = 0
    while result == 0 :
        name = input( "Nhập tên người chơi: " )
        if not is_valid_format( name ):
            print( "Tên chỉ được có các kí tự in hoa, in thường, số và dấu _ " )
            continue
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