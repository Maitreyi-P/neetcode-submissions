class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        hmap = defaultdict(int)
        for c in t:
            hmap[c] += 1
        
        count = len(t)

        window = [0, math.inf]

        l = 0
        r = 0

        while r < len(s):
            if s[l] not in t:
                l += 1 
                r = l
            if r>=len(s):
                break
            if s[r] in t:
                if hmap[s[r]] > 0:
                    hmap[s[r]] -= 1
                    count -= 1
                r += 1
            elif s[r] not in t and count > 0:
                r += 1
            
            if count == 0:
                if r - l < window[1] - window[0]:
                    window[1] = r
                    window[0] = l
                count = len(t)
                for c in t:
                    hmap[c] += 1
                l += 1
                r = l
        
        if window[1] == math.inf:
            return ""
        res = s[window[0]:window[1]]
        return res
                
