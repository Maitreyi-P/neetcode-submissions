class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = defaultdict(int)
        for t in tasks:
            count[t] += 1

        maxheap = []
        waitq = deque()

        for t,f in count.items():
            heapq.heappush_max(maxheap,f)

        time = 0

        while maxheap or waitq:
            time += 1
            if maxheap:
                curr = heapq.heappop_max(maxheap)
                curr -= 1
                if curr > 0:
                    waitq.append((curr, time+n))

            if waitq and waitq[0][1] == time:
                temp = waitq.popleft()
                heapq.heappush_max(maxheap, temp[0])


        return time