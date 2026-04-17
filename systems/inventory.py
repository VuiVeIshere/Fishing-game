from sprites.fish import Fish
from sprites.player import Player 

class Inventory:
    def __init__( self, player: Player, fish_list: list[Fish] ):
        self.player = player
        self.fish_list = fish_list
    def add_fish( self, fish: Fish ):
        if fish.fish_id in self.player.inventory:
            self.player.inventory[ fish.fish_id ] += 1
        else:
            self.player.inventory[ fish.fish_id ] = 1
    def get_fish_by_id( self, fish_id ):
        for fish in self.fish_list:
            if fish.fish_id == fish_id:
                return fish
        return None
    def show_inventory( self ):
        print( "=== Inventory ===" )
        if not self.player.inventory:
            print( "Bạn chưa câu được con cá nào!" )
            return
        for fish_id, quantity in self.player.inventory.items():
            fish = self.get_fish_by_id( fish_id )
            print( f"{fish.name} - {quantity} con " )
    def sell_fish( self, fish_id = 0, quantity = 0, all = False ):
        if all:
            money = 0
            for fish_id, quantity in self.player.inventory.items():
                money += self.get_fish_by_id( fish_id ).value * quantity
            self.player.coins += money
            self.player.inventory.clear()
            print( f"Bạn đã bán tất cả cá trong kho và được {money} xu!" )
        else:
            if fish_id <= 0 or quantity <= 0:
                print( "Vui lòng nhập ID cá và số lượng hợp lệ!" )
                return
            if fish_id not in self.player.inventory :
                print( "Bạn không có loại cá này trong kho!" )
                return
            if self.player.inventory[ fish_id ] < quantity:
                print( "Bạn không có đủ số lượng cá để bán!" )
                return
            fish = self.get_fish_by_id( fish_id )
            money = fish.value * quantity
            self.player.coins += money
            self.player.inventory[ fish_id ] -= quantity
            if self.player.inventory[ fish_id ] == 0:
                del self.player.inventory[ fish_id ]
            print( f"Bạn đã bán {quantity} con {fish.name} và được {money} xu!" )