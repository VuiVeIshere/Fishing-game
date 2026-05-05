from data.data import Data
class Rod:
    """
    Lưu trữ thông tin cần câu.

    Attributes:
        name (str): Tên cần câu.
        bonus (dict): Các bonus tỉ lệ câu cá.
        
    """
    def __init__( self, name ):
        self.data = Data()
        self.name = name.lower().capitalize()
        self.bonus = self.data.rod_list[ self.name ]
    def to_dict( self ):
        return {
            "name": self.name
        }

    @staticmethod
    def from_dict( data ):
        return Rod( data["name"] )
    