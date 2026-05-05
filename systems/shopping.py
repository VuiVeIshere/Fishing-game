from sprites.player import Player
from data.data import Data
from sprites.rod import Rod
class Shop:
    """
    Hệ thống cửa hàng trong game.

    Cho phép người chơi mua cần câu để tăng hiệu quả câu cá.

    Attributes:
        player (Player): Người chơi thực hiện giao dịch
    """
    def __init__( self, player = Player ):
        """
        Khởi tạo cửa hàng.

        Args:
            player (Player): Người chơi
        """
        self.player = player
        self.data = Data()
    def buy_rod( self, rod_name = "" ):
        """
        Mua cần câu.

        Kiểm tra:
        - Người chơi đã sở hữu chưa
        - Có đủ tiền hay không

        Args:
            rod_name (str): Tên cần câu

        Returns:
            Kết quả khi câu cá
        """
        if rod_name == "":
            print( "Bạn vào đây mà không mua gì ?" )
        else:
            if rod_name not in self.data.rod_list:
                print( "Ở đây không bán cần này rồi bạn." )
            else: 
                if self.player.rod_state[ rod_name ]:
                    self.player.equip_rod( Rod( rod_name ) )
                    print( f"Đã sử dụng {rod_name}.")
                else:
                    price = self.data.rod_list[ rod_name ][ "price" ]
                    player_money = self.player.coins
                    if price > player_money:
                        print( "Ráng câu thêm cá nữa đi, bạn chưa đủ tiền mua cần này!" )
                    else:
                        self.player.coins -= price
                        self.player.equip_rod( Rod( rod_name ) )
                        self.player.rod_state[ rod_name ] = True
                        print( f"Bạn đã mua thành công {rod_name}!" )
