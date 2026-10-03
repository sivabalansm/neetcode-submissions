class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            num_str = ""
            while s[i] != "#":
                num_str += s[i]
                i += 1
            
            num = int(num_str)

            word = s[i + 1: i + 1 + num]
            res.append(word)
            i += 1 + num
        return res
