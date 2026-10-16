class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(c, p):
            for i in range(len(isConnected[c])):
                isConnect = isConnected[c][i]
                if c == i or p == i:
                    isConnected[c][i] = 0
                if isConnect == 1:
                    isConnected[c][i] = 0
                    dfs(i, c)
        res = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    dfs(j, -1)
                    res += 1
        return res


