class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedS = tuple(sorted(s))
            if sortedS not in res:
                res[sortedS] = [s]
            else:
                res[sortedS].append(s)
        return res.values()


   
        