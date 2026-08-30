class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        res = 0
        # 1 2 2 3 3
        while l <= r:
            if l == r:
                s = people[l]
            else:
                s = people[l] + people[r]
            if s < limit or s == limit:
                r -= 1
                l += 1
            else:
                r -= 1
            
            res += 1
        return res