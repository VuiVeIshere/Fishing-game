from sprites.fish import Fish
from sprites.player import Player
from systems.fishing import Fishing
from systems.inventory import Inventory
from systems.hash_utils import Hash
from data.data import Data
from systems.shopping import Shop
class Game():
    def __init__( self, player: Player ):
        self.fish_list = []
        self.player = player
        self.inv = Inventory( self.player )
        self.fishing_system = Fishing( self.player, self.inv )
        self.data = Data()
    def fishing( self ):
        fish = self.fishing_system.select_fish()
        self.inv.add_fish( fish )
        self.player.exp += fish.exp
        print( f"Bạn đã câu được {fish.name} ( {fish.rarity} ) và nhận được {fish.exp} điểm kinh nghiệm!" )
        while self.player.exp >= self.player.level * 100:
            self.player.exp -= self.player.level * 100
            self.player.level += 1
            print( f"Chúc mừng! Bạn đã lên cấp {self.player.level}!" )
    def play( self ):
        while True:
            print( " === Menu ===" )
            print( "1. Đi câu cá" )
            print( "2. Xem kho cá" )
            print( "3. Xem thông tin người chơi" )
            print( "4. Bán cá" )
            print( "5. Mua cần câu")
            print( "6. Thoát" )
            choice = input( "Chọn một hành động: " )
            if choice == "1":
                self.fishing()
            elif choice == "2":
                self.inv.show()
            elif choice == "3":
                self.player.check_info()
            elif choice == "4":
                fish_name = input( "Nhập tên cá muốn bán (nhập all để bán tất cả): " ).strip().lower()
                if fish_name == "all":
                    self.inv.sell_fish( all = True )
                else:
                    quantity_input = input( "Nhập số lượng muốn bán: " ).strip()
                    if not quantity_input.isdigit():
                        print( "Số lượng phải là số nguyên dương!" )
                        continue
                    self.inv.sell_fish( fish_name , int( quantity_input ) )
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
                print( "Cảm ơn bạn đã chơi!" )
                break
