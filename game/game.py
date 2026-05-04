from sprites.fish import Fish
from sprites.player import Player
from systems.fishing import Fishing
from systems.inventory import Inventory
from systems.hash_utils import Hash
from data.data import Data
from systems.shopping import Shop
from systems.save import Save
import threading
import time
class Game:
    def __init__( self, player: Player, save, fish_list = [] ):
        self.fish_list = fish_list
        self.player = player
        self.inv = Inventory( self.player, self.fish_list )
        self.fishing_system = Fishing( self.player, self.inv )
        self.data = Data()
        self.save = save 
    def fishing( self ):
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
    def listen_input( self ):
        while True:
            cmd = input()
            if cmd == "q" :
                self.running = False
                break
    def play( self ):
        while True:
            print( " === Menu ===" )
            print( "1. Đi câu cá" )
            print( "2. Xem kho cá" )
            print( "3. Xem thông tin người chơi" )
            print( "4. Bán cá" )
            print( "5. Mua cần câu")
            print( "6. Sắp xếp kho cá" )
            print( "7. Thoát" )
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
                self.save.save_player()    
                print( "Cảm ơn bạn đã chơi!" )
                break
