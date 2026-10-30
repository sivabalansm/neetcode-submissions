class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        mah = [val for val in freq.values()]
        heapq.heapify_max(mah)
        q = deque()

        time = 0
        while mah or q:
            if not mah:
                time = q[0][0]
            
            while q and time >= q[0][0]:
                _, t = q.popleft()
                heapq.heappush_max(mah, t)

            t = heapq.heappop_max(mah)
            t -= 1
            time += 1
            if t > 0:
                q.append((time + n, t))
        return time
