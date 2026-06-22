class Solution:
    def firstUniqChar(self, s: str) -> int:


        hmap = defaultdict(list)

        for i in range(len(s)):
            hmap[s[i]].append(i)

        res = []
        
        for k, v in hmap.items():
            if len(v) == 1:
                res.append(v[0])
            
        if res:
            return min(res)
        return -1
        