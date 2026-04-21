
class Hash:
    def __init__( self, buckets ):
        self.quantity = buckets
        self.table = [ [] for _ in range( self.quantity ) ]
    def insert( self, key ):
        idx = self.get_hash_index( key )
        if key not in self.table[ idx ]:
            self.table[ idx ].append( key )
    def remove( self, key ):
        idx = self.get_hash_index( key )
        if key in self.table[ idx ]:
            self.table[ idx ].remove( key )
    def get_hash_index( self, key ):
        val = 0
        for c in key:
            val = ( val * 31 + ord( c ) ) % self.quantity
        return val