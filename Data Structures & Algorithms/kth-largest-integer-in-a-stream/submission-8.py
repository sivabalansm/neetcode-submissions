class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.mh = []
        for num in nums:
            heapq.heappush(self.mh, num)
            if len(self.mh) > k:
                heapq.heappop(self.mh)
        print(self.mh)

    def add(self, val: int) -> int:
        heapq.heappush(self.mh, val)
        if len(self.mh) > self.k:
            heapq.heappop(self.mh)
        return self.mh[0]
