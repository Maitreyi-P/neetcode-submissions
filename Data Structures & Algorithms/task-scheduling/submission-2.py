class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = {}
        for t in tasks:
            if t in count:
                count[t] += 1
            else:
                count[t] = 1

        maxheap = []

        for t,c in count.items():
            heapq.heappush_max(maxheap, (c,t))

        time = 0

        q = deque()

        while maxheap or q:
            time += 1

            if maxheap:
                count, task = heapq.heappop_max(maxheap)
                count -= 1
                if count > 0:
                    q.append((count, task, time + n))

            if q and q[0][2] == time:
                heapq.heappush_max(maxheap,(q[0][0],q[0][1]))
                q.popleft()

        return time
