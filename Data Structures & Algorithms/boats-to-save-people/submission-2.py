class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        k = 0
        # 1 2 2 3 3 
        while l <= r:
            remain = limit - people[r]
            r -= 1
            if remain >= people[l]:
                l += 1
            k += 1
        return k
