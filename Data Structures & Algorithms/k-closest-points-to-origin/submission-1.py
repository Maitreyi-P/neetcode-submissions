class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minheap = []


        for x,y in points:
            dist = (x**2)+(y**2)  #no need to find sqrt because if sum is bigger, sqrt will also be bigger
            minheap.append([dist,x,y])

        heapq.heapify(minheap)

        res=[]
        while k> 0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x,y])
            k-=1

        return res