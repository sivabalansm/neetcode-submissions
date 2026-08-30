class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""

        for s in strs:
            word += f"{len(s)}#{s}"
        return word

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            end = s.find("#", i)
            num = int(s[i:end])

            word = s[end + 1:end + 1 + num]
            res.append(word)
            i = end + 1 + num
        return res

