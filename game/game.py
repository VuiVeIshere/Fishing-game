from sprites.fish import Fish
from sprites.player import Player
from systems.fishing import Fishing
from systems.inventory import Inventory

class Game():
    def __init__( self, fish_list: list[Fish], player: Player ):
        self.fish_list = fish_list
        self.player = player
        self.inv = Inventory( self.player, self.fish_list )
        self.fishing_system = Fishing( self.fish_list, self.player, self.inv )
    def fishing( self ):
        fish = self.fishing_system.select_fish()
        self.inv.add_fish( fish )
        self.player.exp += fish.exp
        rarity_name = { 1: "Common", 2: "Uncommon", 3: "Rare", 4: "Epic", 5: "Legendary" }
        print( f"Bạn đã câu được {fish.name} ( {rarity_name[ fish.rarity ]} ) và nhận được {fish.exp} điểm kinh nghiệm!" )
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
            print( "5. Thoát" )
            choice = input( "Chọn một hành động: " )
            if choice == "1":
                self.fishing()
            elif choice == "2":
                inv = self.inv 
                inv.show_inventory()
            elif choice == "3":
                self.player.check_info()
            elif choice == "4":
                id = input( "Nhập ID cá muốn bán ( nhập all để bán tất cả): " )
                if id == "all":
                    self.inv.sell_fish( all = True )
                else:
                    quantity = int( input( "Nhập số lượng muốn bán: " ) )
                    self.inv.sell_fish( int( id ), quantity )
            elif choice == "5":
                print( "Cảm ơn bạn đã chơi!" )
                break