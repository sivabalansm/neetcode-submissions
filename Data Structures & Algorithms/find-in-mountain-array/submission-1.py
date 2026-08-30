class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        cache = {}
        # genius who found this
        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        # find peak
        l, r = 1, length - 2
        m = 0
        while l <= r:
            m = (l + r) // 2
            left, mid, right = get(m - 1), get(m), get(m + 1)

            if left > mid > right:
                r = m - 1
            elif left < mid < right:
                l = m + 1
            else:
                break
        peak = m
        print(peak)
        l = 0
        r = peak
        while l <= r:
            m = (l + r) // 2
            if target < get(m):
                r = m - 1
            elif get(m) < target:
                l = m + 1
            else:
                return m
        l = peak
        r = length - 1
        while l <= r:
            m = (l + r) // 2
            if get(m) > target:
                l = m + 1
            elif target > get(m):
                r = m - 1
            else:
                return m
        return - 1
        