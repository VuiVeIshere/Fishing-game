import random
dict_fish = {   # fish_name : rarity name and rarity default = 0
    "Cá chép" : { "rarity": "Common", "rate": 40, "weight": 2 },
    "Cá trắm" : { "rarity": "Uncommon", "rate": 30, "weight": 4 },
    "Cá hồi" : { "rarity": "Rare", "rate": 15, "weight": 6 },
    "Cá mập" : { "rarity": "Legendary", "rate": 5, "weight": 400 },
    "Cá vàng" : { "rarity": "Epic", "rate": 10, "weight": 1 },
    "Cá Hải tượng" : { "rarity": "Legendary", "rate": 5, "weight": 350 },
    "Cá trê" : { "rarity": "Common", "rate": 40, "weight": 5 }
}
rod_list = {    #GPT help build
    "Cần cơ bản": {
        "bonus": {},
        "price": 0
    },
    "Cần gỗ": {
        "bonus": {
            "Uncommon": 1.2,
            "Rare": 1.1
        },
        "price": 5000
    },
    "Cần đá": {
        "bonus": {
            "Uncommon": 1.4,
            "Rare": 1.2
        },
        "price": 12000
    },
    "Cần sắt": {
        "bonus": {
            "Uncommon": 1.4,
            "Rare": 1.4,
            "Epic": 1.1
        },
        "price": 20000
    },
    "Cần bạc": {
        "bonus": {
            "Uncommon": 1.4,
            "Rare": 1.7,
            "Epic": 1.3
        },
        "price": 30000
    },
    "Cần vàng": {
        "bonus": {
            "Uncommon": 1.4,
            "Rare": 1.5,
            "Epic": 1.3,
            "Legendary": 1.2
        },
        "price": 35000
    },
    "Cần kim cương": {
        "bonus": {
            "Uncommon": 1.4,
            "Rare": 1.5,
            "Epic": 1.1,
            "Legendary": 1.4
        },
        "price": 55000
    }
}
class Data:
    def __init__ ( self ):
        self.dict_fish = dict_fish
        self.rod_list = rod_list

