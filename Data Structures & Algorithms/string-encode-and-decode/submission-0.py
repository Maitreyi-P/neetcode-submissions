class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            val = len(s)
            res = res + str(val) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l = ""
            while s[i] != "#":
                l += s[i]
                i+=1
            length = int(l)
            res.append(s[i+1:i+length+1])
            i = i+length+1
        return res
        