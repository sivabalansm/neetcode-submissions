class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        s = 0
        sg = gas[s] - cost[s]
        for i in range(1, len(gas)):
            ig = gas[i] - cost[i]
            if ig > sg:
                print(i, ig)
                s = i
                sg = ig
        return s
