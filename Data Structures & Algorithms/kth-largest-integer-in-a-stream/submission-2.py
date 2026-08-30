import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """
        heapq.heappush(self.minHeap, val)
        print(self.minHeap)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        """
        heapq.heappushpop(self.minHeap, val)
        return self.minHeap[0]

