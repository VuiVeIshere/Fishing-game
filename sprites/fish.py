class Fish:
    def __init__( self, fish_id, name, rarity, weight ):
        self.fish_id = fish_id                      # ID của cá
        self.name = name                            # tên cá
        self.rarity = rarity                        # độ hiếm (Common - 1, Uncommon - 2, Rare - 3, Epic - 4, Legendary - 5)
        self.value = rarity * 100 + weight * 10     # giá bán
        self.weight = weight                        # trọng lượng
        self.exp = self.value // 10                 # điểm kinh nghiệm khi câu được