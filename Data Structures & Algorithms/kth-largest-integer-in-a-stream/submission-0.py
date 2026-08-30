import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.nums = nums[-k + 1:]
        self.k = k

    def add(self, val: int) -> int:

        return heapq.heappushpop(self.nums, val)

