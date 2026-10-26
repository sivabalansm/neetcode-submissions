class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = Counter(t)
        need = len(t_freq)
        freq = defaultdict(int)
        have = 0
        l = 0
        res = [-1, -1]
        rsize = float("inf")
        for r in range(len(s)):
            c = s[r]
            freq[c] += 1
            if c in t_freq and freq[c] == t_freq[c]:
                have += 1
            
            while have == need:
                c = s[l]
                if c in t_freq:
                    if freq[c] == t_freq[c]:
                        have -= 1
                    if r - l + 1 < rsize:
                        rsize = r - l + 1
                        res = [l, r]
                    
                freq[c] -= 1
                if freq[c] == 0:
                    del freq[c]
                l += 1
        return s[res[0]: res[1] + 1]

