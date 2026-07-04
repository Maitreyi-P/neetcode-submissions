class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        maxheap = []

        for val, f in freq.items():
            heapq.heappush_max(maxheap,(f,val))

        print(maxheap)
        
        prev = None
        res = ""

        while maxheap or prev:
            if prev and not maxheap:
                return ""
                
            f, char = heapq.heappop_max(maxheap)
            res += char
            f -= 1

            if prev:
                heapq.heappush_max(maxheap,prev)
                prev = None
            
            if f > 0:
                prev = (f,char)

        return res
