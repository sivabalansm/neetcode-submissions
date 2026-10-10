class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) == 2:
            return min(cost)
        one = 0
        two = 0
        for i in range(2, len(cost) + 1):
            tmp2 = two
            two = min(two + cost[i - 1], one + cost[i - 2])
            one = tmp2

        return two