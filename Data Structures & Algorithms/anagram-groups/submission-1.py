class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedS = tuple(sorted(s))
            res[sortedS].append(s)
        return res.values()


   
        