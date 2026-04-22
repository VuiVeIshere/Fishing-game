from sprites.player import Player
from data.data import Data
from sprites.rod import Rod
class Shop:
    def __init__( self, player = Player ):
        self.player = player
        self.data = Data()
    def buy_rod( self, rod_name = "" ):
        #In danh sách và bảng giá
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
