from data.data import Data
class Rod:
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
    