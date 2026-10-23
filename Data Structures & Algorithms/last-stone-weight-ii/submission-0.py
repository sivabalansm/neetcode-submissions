class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)

            heapq.heappush_max(stones, abs(s1 - s2))
        
        return stones[0]
