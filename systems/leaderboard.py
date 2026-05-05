import heapq

class Leaderboard:
    """
    Quản lý bảng xếp hạng người chơi.

    Lưu trữ và sắp xếp người chơi dựa trên:
    - Số tiền (coins)
    - Cấp độ (level)

    Attributes:
        data (dict): Dữ liệu người chơi (tên, coin, level)
    """
    def __init__(self):
        
        # max heap giả (dùng -value)
        self.coin_heap = []
        self.level_heap = []

        # lưu score thật
        self.coin_map = {}
        self.level_map = {}

    def update(self, username, coin=None, level=None):
        """
        Cập nhật thông tin người chơi.

        Args:
            name (str): Tên người chơi
            coins (int): Số tiền
            level (int): Cấp độ
        """
        if coin is not None:
            self.coin_map[username] = coin
            heapq.heappush(self.coin_heap, (-coin, username))

        if level is not None:
            self.level_map[username] = level
            heapq.heappush(self.level_heap, (-level, username))

    def get_top_coin(self, k):
        """
        Lấy top người chơi có nhiều tiền nhất.

        Args:
            n (int): Số lượng người chơi cần lấy

        Returns:
            list: Danh sách (name, coins)
        """
        return self._get_top(self.coin_heap, self.coin_map, k)

    def get_top_level(self, k):
        """
        Lấy top người chơi có level cao nhất.

        Args:
            n (int): Số lượng người chơi cần lấy

        Returns:
            list: Danh sách (name, level)
        """
        return self._get_top(self.level_heap, self.level_map, k)

    def _get_top(self, heap, score_map, k):
        result = []
        temp = []
        if len( heap ) > 2 * len( score_map ):
            self.rebuild()
        while heap and len(result) < k:
            neg_score, username = heapq.heappop(heap)
            score = -neg_score

            # chỉ lấy bản mới nhất
            if score_map.get(username) == score:
                result.append((username, score))
                temp.append((neg_score, username))

        # push lại heap
        for item in temp:
            heapq.heappush(heap, item)

        return result

    def rebuild(self):
        self.coin_heap = [(-v, u) for u, v in self.coin_map.items()]
        heapq.heapify(self.coin_heap)

        self.level_heap = [(-v, u) for u, v in self.level_map.items()]
        heapq.heapify(self.level_heap)