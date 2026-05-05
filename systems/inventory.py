from sprites.fish import Fish
from sprites.player import Player 
from systems.hash_utils import Hash
from data.data import Data
from systems.sort_utils import quick_sort, partition
class Inventory:
    """
    Quản lý kho đồ của người chơi.

    Lưu trữ và xử lý các thao tác liên quan đến cá:
    - Thêm cá vào kho
    - Hiển thị danh sách cá
    - Bán cá
    - Sắp xếp cá

    Attributes:
        player (Player): Người chơi sở hữu kho đồ
        fish_list (list): Danh sách đối tượng Fish
        inventory (Hash): Hashtable lưu số lượng cá theo tên
    """
    def __init__( self, player: Player, fish_list = [] ):
        """
        Khởi tạo kho đồ.

        Args:
            player (Player): Người chơi
            fish_list (list, optional): Danh sách cá ban đầu
        """
        self.player = player
        self.fish_list = fish_list
        self.load_inventory()
    def add_fish( self, fish: Fish ):
        self.fish_list.append( fish )
        self.player.inventory.insert( fish.name, 1 )
    def load_inventory( self ):
        """
        Tải lại dữ liệu kho đồ từ danh sách fish_list.

        Duyệt qua danh sách cá và cập nhật số lượng
        vào hashtable inventory.
        """
        for fish in self.fish_list:
            self.player.inventory.insert( fish.name, 1 ) 
    def show( self ):
        """
        Hiển thị danh sách cá trong kho đồ.

        In ra tên cá và số lượng tương ứng.
        """
        print( "====Inventory====")
        if not self.player.inventory:
            print( "Túi đồ của bạn không có gì :( ")
        else:
            for fish in self.fish_list:
                print( f"{fish.name} -  {fish.rarity} - {fish.weight} kg " )
            print("======")
            for bucket in self.player.inventory.table:
                for name, quantity in bucket:
                    print( name, quantity )
    def sell_fish( self, fish_name = "", quantity = 0, all = 0 ):
        """
        Bán cá trong kho đồ.

        Args:
            name (str, optional): Tên cá cần bán
            quantity (int, optional): Số lượng cần bán
            all (bool, optional): Nếu True thì bán toàn bộ cá

        Returns:
            int: Tổng số tiền nhận được
        """
        money = 0
        if all:
            for fish in self.fish_list:
                money += fish.value
            self.player.inventory.clear_()
            self.fish_list.clear()
            print( f"Bạn đã bán tất cả cá trong kho và được {round( money, 2 )} xu!" )
        else:
            if fish_name == "" or quantity == 0:
                print( "Bạn không bán cá gì hoặc không bán con cá nào ư?" )
            else:
                fish_name = fish_name.capitalize()
                if self.player.inventory.get( fish_name ) == 0:
                        print( f"Túi đồ của bạn không có cá {fish_name}!" )
                elif quantity <= 0 or quantity > self.player.inventory.get( fish_name ):
                        print( f"Số lượng cá muốn bán không hợp lệ!" )
                else:
                    for i in range ( quantity ):
                        for fish in self.fish_list:
                            if fish.name == fish_name:
                                money += fish.value
                                self.fish_list.remove( fish )
                                self.player.inventory.remove( fish_name, 1 )
                                break
                    print( f"Bạn đã bán {quantity} con cá {fish_name} và được {round( money, 2 )} xu!" )
        self.player.coins = round( self.player.coins + round( money, 2 ), 2 )
        print( f"Bạn hiện đang có {self.player.coins} xu!" )
    def sort( self, key = lambda x: x ):
        """
        Sắp xếp danh sách cá theo tiêu chí cho trước.

        Args:
            key (function): Hàm xác định tiêu chí sắp xếp
        """
        sorted_a = quick_sort( self.fish_list, key = key )
        for element in sorted_a:
            print( f"{element.name} -  {element.rarity} - {element.weight} kg " )
