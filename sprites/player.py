from sprites.rod import Rod
class Player:
    def __init__( self, player_name, level = 1, exp = 0, coins = 0, inventory = {}, hash_to_name = {}, rod = Rod( "Cần cơ bản" ), rod_state = { "Cần cơ bản": True, "Cần gỗ": False, "Cần đá": False, "Cần sắt": False, "Cần bạc": False, "Cần vàng": False, "Cần kim cương": False } ):
        self.player_name = player_name  # ID của người chơi
        self.level = level             # cấp độ
        self.exp = exp                # điểm kinh nghiệm
        self.coins = coins              # số xu
        self.inventory = inventory        # danh sách cá đã câu được { hash_fish: quantity }
        self.hash_to_name = hash_to_name
        self.rod = rod
        self.rod_state = rod_state
        self.rod_name = self.rod.name 
        self.rod_bonus = self.rod.bonus
    def check_info( self ):
        print( f"=== Thông tin người chơi ===" )
        print( f"Tên: {self.player_name}" )
        print( f"Cấp độ: {self.level}" )
        print( f"Cần câu: {self.rod_name}")
        print( f"Điểm kinh nghiệm: {self.exp}" )
        print( f"Số xu: {self.coins}" )
    def equip_rod(self, rod = Rod ):
        self.rod = rod
        self.rod_name = self.rod.name 
        self.rod_bonus = self.rod.bonus
    def to_dict(self):
        return {
            "player_name": self.player_name,
            "level": self.level,
            "exp": self.exp,
            "coins": self.coins,
            "inventory": self.inventory,
            "hash_to_name": self.hash_to_name,
            "rod": self.rod.to_dict(),
            "rod_state": self.rod_state
        }
    @staticmethod
    def from_dict( data):
        return Player(
            data["player_name"],
            data["level"],
            data["exp"],
            data["coins"],
            data["inventory"],
            data["hash_to_name"],
            Rod.from_dict( data["rod"] ),
            data["rod_state"]
        )
