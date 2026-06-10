class MedianFinder:

    def __init__(self):
        # 2 heaps - large(minheap) small(maxheap)
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, (-1 * heapq.heappop(self.small)))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, (-1 * heapq.heappop(self.small)))

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, (-1 * heapq.heappop(self.large)))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0])/2
        