class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l = 0
        r = len(people) - 1
        """
        1 2 2 3 3

        """
        while l <= r:
                
            nl = people[l]
            nr = people[r]
            if l == r:
                nr = 0
                
            if nl + nr > limit:
                res += 1
                r -= 1
            else:
                res += 1
                l += 1
                r -= 1
        return res
            