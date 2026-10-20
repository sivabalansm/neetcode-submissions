class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0
        while q:
            idx = q.popleft()
            start = max(idx + minJump, farthest)
            end = min(idx + maxJump + 1, len(s))
            for i in range(start, end):
                if s[i] == "0":
                    q.append(i)
                    if i == len(s) - 1:
                        return True
            farthest = idx + maxJump
        return False


