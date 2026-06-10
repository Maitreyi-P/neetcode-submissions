class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxl = 0
        i=0
        j=0

        seen = []
        while j<len(s):
            if s[j] not in seen:
                seen.append(s[j])
                j+=1
                maxl = max(maxl,len(seen))
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i+=1
        return maxl