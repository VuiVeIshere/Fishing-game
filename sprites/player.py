class Player:
    def __init__( self, player_id ):
        self.player_id = player_id  # ID của người chơi
        self.level = 1              # cấp độ
        self.exp = 0                # điểm kinh nghiệm
        self.coins = 0              # số xu
        self.inventory = {}         # danh sách cá đã câu được
    def check_info( self ):
        print( f"=== Thông tin người chơi ===" )
        print( f"ID: {self.player_id}" )
        print( f"Cấp độ: {self.level}" )
        print( f"Điểm kinh nghiệm: {self.exp}" )
        print( f"Số xu: {self.coins}" )