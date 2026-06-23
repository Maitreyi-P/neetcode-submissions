class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
            
        l = 0
        r = 1
        maxlen = 0
        seen = set()
        seen.add(s[0])

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            currlen = r-l
            maxlen = max(maxlen,currlen)

        return maxlen

                