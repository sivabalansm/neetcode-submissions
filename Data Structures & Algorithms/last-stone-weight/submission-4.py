class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mah = [-s for s in stones]
        heapq.heapify(mah)

        while len(mah) > 1:
            x = heapq.heappop(mah)
            y = heapq.heappop(mah)
            if y > x:
                heapq.heappush(mah, x - y)
        mah.append(0)
        return abs(mah[0])

        