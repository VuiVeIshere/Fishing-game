class Fish:
    """
    Lưu trữ thông tin cá.

    Attributes:
        name (str): Tên cá.
        rarity (str): Độ hiếm.
        weight (float): Khối lượng cá.
        value (float): Giá trị của cá ( số tiền có được khi bán )
        exp (int): Kinh nghiệm nhận được.
        
    """
    def __init__( self, name, rarity, weight ):
        self.name = name                                
        self.rarity = rarity
        self.weight = weight                           
        self.rarity_val = {
            "Common": 1,
            "Uncommon": 2,
            "Rare": 3,
            "Epic": 4,
            "Legendary": 5
        }
        self.value = float( self.rarity_val[ self.rarity ] * 10 + self.weight * 2 )    
        self.exp = int( self.value // 10 )             
    def to_dict( self ):
        return {
            "name": self.name,
            "rarity": self.rarity,
            "weight": self.weight
        }
    @staticmethod
    def from_dict( data ):
        return Fish(
            data["name"],
            data["rarity"],
            data["weight"]
        )
