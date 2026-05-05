from sprites.fish import Fish
from sprites.player import Player
from systems.fishing import Fishing
from systems.inventory import Inventory
from systems.hash_utils import Hash
from data.data import Data
from systems.shopping import Shop
from systems.save import Save
from systems.leaderboard import Leaderboard
import threading
import time
class Game:
    """
    Lớp điều khiển chính của trò chơi.

    Quản lý toàn bộ luồng hoạt động của game, bao gồm:
    - Câu cá
    - Quản lý kho đồ
    - Tương tác menu người chơi
    - Mua bán vật phẩm
    - Cập nhật bảng xếp hạng

    Attributes:
        player (Player): Đối tượng người chơi
        fish_list (list): Danh sách cá đã câu được
        inv (Inventory): Hệ thống quản lý kho đồ
        fishing_system (Fishing): Hệ thống câu cá
        data (Data): Dữ liệu game (cần câu, cá, ...)
        save (Save): Hệ thống lưu game
        leaderboard (Leaderboard): Bảng xếp hạng người chơi
        
    """
    def __init__( self, player: Player, save, fish_list = [], leaderboard = Leaderboard() ):
        """
        Khởi tạo game với người chơi và các hệ thống liên quan.

        Args:
            player (Player): Người chơi
            save (Save): Đối tượng xử lý lưu game
            fish_list (list, optional): Danh sách cá ban đầu
            leaderboard (Leaderboard, optional): Bảng xếp hạng
        """
        self.fish_list = fish_list
        self.player = player
        self.inv = Inventory( self.player, self.fish_list )
        self.fishing_system = Fishing( self.player, self.inv )
        self.data = Data()
        self.save = save 
        self.leaderboard = leaderboard
    def fishing( self ):
        """
        Thực hiện hành động câu cá.

        - Chọn cá ngẫu nhiên dựa trên hệ thống fishing
        - Thêm cá vào inventory
        - Cộng EXP cho người chơi
        - Hiển thị hiệu ứng đang câu cá
        - Xử lý lên cấp và cập nhật leaderboard
        """
        fish = self.fishing_system.select_fish()
        self.inv.add_fish( fish )
        self.player.exp += fish.exp
        self.rarity_val = fish.rarity_val[ fish.rarity ]
        i = 0
        while self.rarity_val > 0:
                print("Đang câu cá" + "." * ( i % 4 ), end="\r", flush=True)
                time.sleep( 0.5 )
                i += 1 
                self.rarity_val -= 0.5
        print( f"Bạn đã câu được {fish.name} ( {fish.rarity} ) và nhận được {fish.exp} điểm kinh nghiệm!" )
        while self.player.exp >= self.player.level * 100:
            self.player.exp -= self.player.level * 100
            self.player.level += 1
            print( f"Chúc mừng! Bạn đã lên cấp {self.player.level}!" )
            self.leaderboard.update( self.player.player_name, self.player.coins, self.player.level )
    def listen_input( self ):
        while True:
            cmd = input()
            if cmd == "q" :
                self.running = False
                break
    def play( self ):
        """
        Vòng lặp chính của game.

        Hiển thị menu và xử lý các lựa chọn của người chơi:
        1. Câu cá (có hỗ trợ auto fishing bằng threading)
        2. Xem kho đồ
        3. Xem thông tin người chơi
        4. Bán cá
        5. Mua cần câu
        6. Sắp xếp kho đồ
        7. Xem bảng xếp hạng
        8. Thoát game và lưu dữ liệu
        """
        while True:
            print( " === Menu ===" )
            print( "1. Đi câu cá" )
            print( "2. Xem kho cá" )
            print( "3. Xem thông tin người chơi" )
            print( "4. Bán cá" )
            print( "5. Mua cần câu")
            print( "6. Sắp xếp kho cá" )
            print( "7. Xem bảng xếp hạng" )
            print( "8. Thoát" )
            choice = input( "Chọn một hành động: " )
            if choice == "1":
                print("=== Treo máy ( nhấn q để thoát ) ===")
                self.running = True
                threading.Thread( target= self.listen_input , args = (), daemon = False ).start()  
                while self.running:
                    self.fishing()
                    time.sleep(2)
            elif choice == "2":
                self.inv.show()
            elif choice == "3":
                self.player.check_info()
            elif choice == "4":
                fish_name = input( "Nhập tên cá muốn bán (nhập all để bán tất cả): " ).strip().lower()
                if fish_name == "all":
                    self.inv.sell_fish( all = True )
                    self.leaderboard.update( self.player.player_name, self.player.coins, self.player.level )
                else:
                    quantity_input = input( "Nhập số lượng muốn bán: " ).strip()
                    if not quantity_input.isdigit():
                        print( "Số lượng phải là số nguyên dương!" )
                        continue
                    self.inv.sell_fish( fish_name , int( quantity_input ) )
                    self.leaderboard.update( self.player.player_name, self.player.coins, self.player.level )
            elif choice == "5":
                self.shop = Shop( self.player )
                print( "===Shop Câu Cá===" )
                print( "Danh sách cần câu: " )
                self.rod_list = self.data.rod_list
                for name in self.rod_list.keys():
                    if self.player.rod_state[ name ]:
                        print( f"{name} - giá {self.rod_list[ name ][ "price" ]} xu - Đã sở hữu." )
                    else:
                        print( f"{name} - giá {self.rod_list[ name ][ "price" ]} xu - Chưa sở hữu." )
                rod_name = input( "Hãy chọn cần câu bạn muốn mua: " ).strip().lower().capitalize()
                self.shop.buy_rod( rod_name )
            elif choice == "6": 
                key = str( input( "Bạn muốn sắp xếp theo khối lượng, độ hiếm hay theo tên? " ) ).lower().capitalize()
                if key == "Khối lượng":
                    self.inv.sort( lambda x: x.weight )
                elif key == "Độ hiếm":
                    self.inv.sort( lambda x: x.rarity_val[ x.rarity ] )
                elif key == "Tên":
                    self.inv.sort( lambda x: x.name )
                else:
                    print( "Vui lòng chọn đúng tiêu chí. " )
            elif choice == "7":
                print("=== TOP COIN ===")
                for i, (name, coin) in enumerate( self.leaderboard.get_top_coin( 5 ), 1 ):
                    print(f"{i}. {name} - {coin}")
                print("\n=== TOP LEVEL ===")
                for i, (name, lv) in enumerate( self.leaderboard.get_top_level( 5 ), 1 ):
                    print(f"{i}. {name} - Lv {lv}")
            elif choice == "8":
                self.save.save_player()    
                print( "Cảm ơn bạn đã chơi!" )
                break
