from sprites.fish import Fish
from sprites.player import Player
from systems.fishing import Fishing
from systems.inventory import Inventory
from game.game import Game
from systems.hash_utils import Hash
from data.data import Data
def main():
    player = Player( 1 )
    game = Game( player )
    game.play()
if __name__ == "__main__":
    main()