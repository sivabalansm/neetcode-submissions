class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            enc = f"{len(s)}#{s}"
            res.append(enc)
        print(res)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        ls = len(s)
        i = 0
        while i < len(s):
            ns = i
            print("ns", ns)
            while s[i] != "#":
                print("s[i]", s[i])
                i += 1
            n = s[ns:i]
            print("n", n)
            n = int(n)
            i += 1
            res.append(s[i : i + n])
            i += n
        return res
            

