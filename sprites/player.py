from sprites.rod import Rod
class Player:
    def __init__( self, player_id, rod = Rod ):
        self.player_id = player_id  # ID của người chơi
        self.level = 1              # cấp độ
        self.exp = 0                # điểm kinh nghiệm
        self.coins = 0              # số xu
        self.inventory = {}         # danh sách cá đã câu được { hash_fish: quantity }
        self.hash_to_name = {}
        self.rod = rod
        self.rod_state = {
            "Cần cơ bản": True,
            "Cần gỗ": False,
            "Cần đá": False,
            "Cần sắt": False,
            "Cần bạc": False,
            "Cần vàng": False,
            "Cần kim cương": False
        }
        self.rod_name = self.rod.name 
        self.rod_bonus = self.rod.bonus
    def check_info( self ):
        print( f"=== Thông tin người chơi ===" )
        print( f"ID: {self.player_id}" )
        print( f"Cấp độ: {self.level}" )
        print( f"Cần câu: {self.rod_name}")
        print( f"Điểm kinh nghiệm: {self.exp}" )
        print( f"Số xu: {self.coins}" )
    def equip_rod(self, rod = Rod ):
        self.rod = rod
        self.rod_name = self.rod.name 
        self.rod_bonus = self.rod.bonus

