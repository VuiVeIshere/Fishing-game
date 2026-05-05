class Hash:
    """
    Cấu trúc dữ liệu Hashtable sử dụng để lưu trữ dữ liệu dạng key-value.

    Được sử dụng trong game để quản lý inventory của người chơi,
    giúp truy xuất và cập nhật số lượng cá nhanh chóng.

    Attributes:
        size (int): Kích thước bảng băm
        table (list): Danh sách các bucket (chaining)
    """
    def __init__( self, buckets ):
        """
        Khởi tạo bảng băm.

        Args:
            size (int ): Kích thước bảng băm
            table (list): Mảng/ bảng băm
        """
        self.size = buckets
        self.table = [ [] for _ in range( self.size ) ]

    def get_hash_index( self, key ):
        val = 0
        for c in key:
            val =  (val * 31 + ord(c) ) % self.size
        return val

    def insert( self, key, value ):
        """
        Thêm hoặc cập nhật phần tử trong hashtable.

        Args:
            key (str): Khóa
            value (int): Giá trị tương ứng
        """
        idx = self.get_hash_index(key)
        bucket = self.table[idx]
        for i, ( k, v ) in enumerate( bucket ):
            if k == key:
                bucket[ i ] = ( k, v + value )
                return
        bucket.append( ( key, value ) )

    def get( self, key ):
        """
        Lấy giá trị theo key.

        Args:
            key (str): Khóa cần tìm

        Returns:
            int: Giá trị tương ứng với key (hoặc None nếu không tồn tại)
        """
        idx = self.get_hash_index( key )
        for k, v in self.table[ idx ]:
            if k == key:
                return v
        return 0

    def remove( self, key, quantity ):
        """
        Xóa phần tử khỏi hashtable.

        Args:
            key (str): Khóa cần xóa
        """
        idx = self.get_hash_index( key )
        bucket = self.table[ idx ]

        for i, ( k, v ) in enumerate( bucket ):
            if k == key:
                if v <= quantity:
                    bucket.pop( i )
                else:
                    bucket[ i ] = ( k, v - quantity )
                return
    def clear_( self ):
        self.table = [ [] for _ in range( self.size ) ]