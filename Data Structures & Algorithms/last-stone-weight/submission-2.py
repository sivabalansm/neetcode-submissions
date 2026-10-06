class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mah = []
        for stone in stones:
            heapq.heappush(mah, -stone)
        while len(mah) >= 2:
            x = heapq.heappop(mah)
            y = heapq.heappop(mah)
            if abs(x - y) != 0:
                heapq.heappush(mah, abs(x -y))
        
        return mah[0] if len(mah) > 0 else 0

        