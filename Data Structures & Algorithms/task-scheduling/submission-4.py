"""
A B C A I I A 



"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        mah = [val for val in freq.values()]
        heapq.heapify_max(mah)
        cooldown = deque()

        time = 0
        while mah or cooldown:
            if not mah:
                time = cooldown[0][0]
            
            while cooldown and cooldown[0][0] <= time:
                _, task = cooldown.popleft()
                heapq.heappush_max(mah, task)

            task = heapq.heappop_max(mah)

            task -= 1
            time += 1
            if task:
                cooldown.append((time + n, task))

        return time
