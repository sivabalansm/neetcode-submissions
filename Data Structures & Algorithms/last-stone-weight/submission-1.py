import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def smash(x, y):
            return max(x, y) - min(x, y)
        stones = [-stone for stone in stones]   
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            s = smash(x, y)
            heapq.heappush(stones, -s)
        return -stones[0]
            
        
