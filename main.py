from sprites.fish import Fish
from sprites.player import Player
from systems.fishing import Fishing
from systems.inventory import Inventory
from game.game import Game
from systems.hash_utils import Hash
from data.data import Data
from sprites.rod import Rod
from systems.shopping import Shop
def main():
    player = Player( 1, Rod( "Cần cơ bản" ) )
    game = Game( player )
    game.play()
if __name__ == "__main__":
    main()