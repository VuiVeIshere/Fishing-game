import heapq

class Leaderboard:
    def __init__(self):
        # max heap giả (dùng -value)
        self.coin_heap = []
        self.level_heap = []

        # lưu score thật
        self.coin_map = {}
        self.level_map = {}

    # ========================
    # UPDATE
    # ========================
    def update(self, username, coin=None, level=None):
        if coin is not None:
            self.coin_map[username] = coin
            heapq.heappush(self.coin_heap, (-coin, username))

        if level is not None:
            self.level_map[username] = level
            heapq.heappush(self.level_heap, (-level, username))

    # ========================
    # GET TOP
    # ========================
    def get_top_coin(self, k):
        return self._get_top(self.coin_heap, self.coin_map, k)

    def get_top_level(self, k):
        return self._get_top(self.level_heap, self.level_map, k)

    # core logic
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

    # ========================
    # REBUILD (cleanup heap)
    # ========================
    def rebuild(self):
        self.coin_heap = [(-v, u) for u, v in self.coin_map.items()]
        heapq.heapify(self.coin_heap)

        self.level_heap = [(-v, u) for u, v in self.level_map.items()]
        heapq.heapify(self.level_heap)