class Solution:
    def stoneGame(self, piles: List[int]) -> bool:


        def dfs(l, r):
            if l > r:
                return 0 

            even = (r - l + 1) % 2 == 0 # odd means turn of bob

            left = piles[l] if even else 0
            right = piles[r] if even else 0


            return max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
        res = dfs(0, len(piles) - 1)
        s = sum(piles)
        
        return s - res < res
