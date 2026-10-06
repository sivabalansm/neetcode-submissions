class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        2 3 1 5 4
        1 2 3 4 5
              k
        
        """

        mh = []

        for num in nums:
            heapq.heappush(mh, num)
            if len(mh) > k:
                heapq.heappop(mh)
        return mh[0]

        