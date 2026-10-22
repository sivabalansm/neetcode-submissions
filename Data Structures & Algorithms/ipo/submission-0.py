class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        class Node:
            def __init__(self, idx):
                self.idx = idx
            
            def __lt__(self, other):
                if capital[self.idx] != capital[other.idx]:
                    return capital[self.idx] < capital[other.idx]
                return self.idx < other.idx
        
        min_cap = []
        max_profit = []

        for i in range(len(capital)):
            heapq.heappush(min_cap, Node(i))

        for _ in range(k):
            while min_cap and capital[min_cap[0].idx] <= w:
                heapq.heappush_max(max_profit, profits[heapq.heappop(min_cap).idx])
            
            if not max_profit:
                break
            
            w += heapq.heappop_max(max_profit)
        return w

        