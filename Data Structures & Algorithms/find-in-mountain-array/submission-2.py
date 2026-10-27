class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        cache = { -1 : float("-inf"), length : float("inf") }
        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        l = 0
        r = length - 1

        while l < r:
            m = (l + r) // 2

            left = get(m - 1)
            val = get(m)
            right = get(m + 1)

            if left > val > right:
                l = m + 1
            elif left < val < right:
                r = m - 1
            else:
                l = m
                break
        
        if target == get(l):
            return l
        elif target > get(l):
            return -1
        infl = l

        l = 0
        r = infl
        while l <= r:
            m = (l + r) // 2
            if get(m) < target:
                l = m + 1
            elif get(m) > target:
                r = m - 1
            else:
                return m
        
        l = length - 1
        r = infl
        while r <= l:
            m = (l + r) // 2
            if get(m) < target:
                l = m - 1
            elif get(m) > target:
                r = m + 1
            else:
                return m

                


        