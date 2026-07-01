class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        l = 0
        r = 1
        longest = 1

        seen = set()
        seen.add(s[l])

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            longest = max(longest, r - l)

        return longest

