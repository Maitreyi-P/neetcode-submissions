class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        st = set()
        maxlength = 0

        while j<len(s):
            if s[j] not in st:
                st.add(s[j])
                maxlength = max(maxlength, len(st))
                j+=1
            else:
                while s[j] in st:
                    st.remove(s[i])
                    i+=1
        return maxlength

        