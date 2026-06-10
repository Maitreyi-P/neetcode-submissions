class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        j=0
        while i < len(s):
            while s[j]!= '#':
                j+=1
            l = int(s[i:j])
            i = j+1
            j = i+l
            res.append(s[i:j])
            i=j
        return res
        