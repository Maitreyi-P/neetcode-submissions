class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=j=0
        seen = set()
        maxlen = 0

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j+=1
                maxlen = max(maxlen, len(seen))
            else:
              while s[j] in seen:
                seen.remove(s[i])
                i+=1
        return maxlen 
         