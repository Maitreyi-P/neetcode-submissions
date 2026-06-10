class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            hmap[key].append(strs[i])
        return hmap.values()