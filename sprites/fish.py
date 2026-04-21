class Fish:
    def __init__( self, name, rarity, weight ):
        self.name = name                                # tên cá
        self.rarity = rarity                            # độ hiếm (Common - 1, Uncommon - 2, Rare - 3, Epic - 4, Legendary - 5)
        self.value = int( rarity * 10 + weight * 2 )  # giá bán
        self.weight = weight                            # trọng lượng
        self.exp = int( self.value // 10 )              # điểm kinh nghiệm khi câu được