class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        seen = set()
        i = 0
        j = 1
        longest = 0
        seen.add(s[0])

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j+=1
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
            l = j - i
            longest = max(longest,l)

        return longest
        