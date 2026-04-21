from sprites.player import Player
from sprites.fish import Fish
import random
dict_fish = {   # fish_name : rarity
    "Cá chép" : 1,
    "Cá trắm" : 2,
    "Cá hồi" : 3,
    "Cá mập" : 5,
    "Cá vàng" : 4,
    "Cá Hải tượng" : 5,
    "Cá trê" : 1
}
fish_weights = {       # fish_name : weight approx
    "Cá chép" : 2,
    "Cá trắm" : 4,
    "Cá hồi" : 6,
    "Cá mập" : 400,
    "Cá vàng" : 1,
    "Cá Hải tượng" : 350,
    "Cá trê" : 5
}
class Data:
    def __init__ ( self ):
        self.dict_fish = dict_fish
        self.fish_weights = fish_weights
