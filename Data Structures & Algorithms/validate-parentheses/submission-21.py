class Solution:
    def isValid(self, s: str) -> bool:
        compl = { ")": "(", "]" : "[", "}" : "{" }

        st = []

        for p in s:
            if p not in compl:
                st.append(p)
            else:
                c = compl[p]
                if st and st.pop() == c:
                    continue
                return False
        return not st

