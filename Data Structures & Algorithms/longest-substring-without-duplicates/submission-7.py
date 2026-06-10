class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxl = 0
        i = 0
        j = 0
        seen = set()

        count = 0
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j+=1
                maxl = max(maxl,j-i)

            else:
                seen.remove(s[i])
                i+=1

        return maxl