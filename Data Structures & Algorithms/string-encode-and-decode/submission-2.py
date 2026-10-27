class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s

        return res

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):
            n = ""
            while s[i] != "$":
                n += s[i]
                i += 1
            n = int(n)
            res.append(s[i+1:i+n+1])
            i = i+n+1
        
        return res
