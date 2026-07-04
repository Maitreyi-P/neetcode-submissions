class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for s in strs:
            ordstr = [0] * 26
            for i in s:
                ordstr[ord(i) - ord('a')] += 1
            d[str(ordstr)].append(s)

        res = []
        for key, val in d.items():
            res.append(val)

        return res