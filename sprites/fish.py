class Fish:
    def __init__( self, name, rarity, weight ):
        self.name = name                                # tên cá
        self.rarity = rarity
        self.weight = weight                            # trọng lượng
        self.rarity_val = {
            "Common": 1,
            "Uncommon": 2,
            "Rare": 3,
            "Epic": 4,
            "Legendary": 5
        }
        self.value = float( self.rarity_val[ self.rarity ] * 10 + self.weight * 2 )    # giá bán
        self.exp = int( self.value // 10 )              # điểm kinh nghiệm khi câu được