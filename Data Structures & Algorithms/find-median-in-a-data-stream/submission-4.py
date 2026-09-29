class MedianFinder:

    def __init__(self):
        self.minheap = [] #larger half
        self.maxheap = [] #smaller half

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush_max(self.maxheap, num)

        if len(self.maxheap) - len(self.minheap) > 1:
            n = heapq.heappop_max(self.maxheap)
            heapq.heappush(self.minheap, n)

        if len(self.minheap) - len(self.maxheap) > 1:
            n = heapq.heappop(self.minheap)
            heapq.heappush_max(self.maxheap, n)


    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + self.maxheap[0])/2
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return self.maxheap[0]
        