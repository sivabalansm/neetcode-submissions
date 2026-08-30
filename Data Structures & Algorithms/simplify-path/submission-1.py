class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        st = []
        for p in path:
            if st and p == "..":
                st.pop()
            elif p and p != "." and p != "..":
                st.append(p)
            
        return "/" + "/".join(st)