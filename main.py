from sprites.fish import Fish
from sprites.player import Player
from systems.fishing import Fishing
from systems.inventory import Inventory
from game.game import Game

def main():
    fish_list = [
        Fish( 1, "Cá chép", 1, 1.0 ),
        Fish( 2, "Cá trắm", 2, 2.0 ),
        Fish( 3, "Cá hồi", 3, 3.0 ),
        Fish( 4, "Cá mập", 4, 50.0 ),
        Fish( 5, "Cá vàng", 5, 0.5 )
    ]
    player = Player( 1 )
    game = Game( fish_list, player )
    game.play()
if __name__ == "__main__":
    main()