class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda t:t[1]) #sort based on start times
        minheap = [] #end, passengers

        currPass = 0

        for t in trips:
            numPass, start, end = t
            #to check if trips are completed
            while minheap and minheap[0][0] <= start:
                currPass -= minheap[0][1]
                heapq.heappop(minheap)
            currPass += numPass
            if currPass > capacity:
                return False
            heapq.heappush(minheap, [end, numPass])

        return True

