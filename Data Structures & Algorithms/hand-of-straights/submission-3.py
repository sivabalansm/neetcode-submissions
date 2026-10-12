class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        freq = Counter(hand)

        for num in hand:
            if freq[num] > 0:
                check = num
                while check < num + groupSize:
                    if freq[check] > 0:
                        freq[check] -= 1
                        check += 1
                    else:
                        return False
        return True