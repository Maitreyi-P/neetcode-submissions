class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        
        # heapq.heappush_max(self.maxheap,num)
        # if len(self.maxheap) > len(self.minheap) + 1:
        #     top = heapq.heappop_max(self.maxheap)
        #     heapq.heappush(self.minheap,top)

        if self.minheap and self.minheap[0] < num:
            heapq.heappush(self.minheap,num)
        else:
            heapq.heappush_max(self.maxheap,num)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            top = heapq.heappop_max(self.maxheap)
            heapq.heappush(self.minheap,top)

        if len(self.minheap) > len(self.maxheap) + 1:
            top = heapq.heappop(self.minheap)
            heapq.heappush_max(self.maxheap,top)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap):
            return self.maxheap[0]
        else:
            return (self.minheap[0] + self.maxheap[0]) / 2

