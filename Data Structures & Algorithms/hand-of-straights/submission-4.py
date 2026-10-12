class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)

        for num in hand:
            s = num
            while freq[s - 1] > 0:
                s -= 1
            while freq[s] > 0:
                for i in range(s, s + groupSize):
                    if freq[i] <= 0:
                        return False
                    freq[i] -= 1
        return True


