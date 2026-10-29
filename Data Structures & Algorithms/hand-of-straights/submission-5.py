class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        freq = Counter(hand)
        for i in range(len(hand) // groupSize):
            start = min(freq)
            for i in range(groupSize):
                if start + i not in freq:
                    return False
                freq[start + i] -= 1
                if freq[start + i] == 0:
                    del freq[start + i]
        return True


