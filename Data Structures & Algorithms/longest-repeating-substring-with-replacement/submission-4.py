class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
        freq = {}
        l = 0
        r = 0
        maxwindow = 0
        maxf = 0

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1

            maxf = max(maxf, freq[s[r]])
            window = r - l + 1

            if window - maxf <= k:
                r += 1
                maxwindow = max(maxwindow,window)
            else:
                freq[s[l]] -= 1
                l += 1


        return maxwindow

 