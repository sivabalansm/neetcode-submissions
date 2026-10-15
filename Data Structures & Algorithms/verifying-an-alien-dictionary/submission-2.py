class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphaOrder = {c : i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]

            s = min(len(w1), len(w2))
            p1, p2 = 0, 0

            while p1 < s and p2 < s and w1[p1] == w2[p2]:
                p1 += 1
                p2 += 1
            
            # equal prefix
            print(p1, p2, s)
            if (p1 == s or p2 == s) and len(w1) > len(w2):
                return False
            elif (p1 == s or p2 == s) and len(w1) <= len(w2):
                return True
            
            if alphaOrder[w1[p1]] > alphaOrder[w2[p2]]:
                return False
        return True

            

            
