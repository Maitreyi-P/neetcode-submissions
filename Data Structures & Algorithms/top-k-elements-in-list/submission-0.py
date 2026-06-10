class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            countdict[n] = 1 + countdict.get(n,0)
        for n,c in countdict.items():
            freq[c].append(n)

        res = []
        for  i in range(len(freq)-1, 0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


