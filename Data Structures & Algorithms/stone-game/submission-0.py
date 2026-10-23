class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        owe = len(piles) // 2

        s = sum(piles)

        