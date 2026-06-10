class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()

        while maxheap or q:

            if not maxheap:
                time = q[0][1]

            else:
                time+=1
                taskcount = 1+ heapq.heappop(maxheap)
                if taskcount:
                    q.append([taskcount,time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q[0][0])
                q.popleft()

        return time
