class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in range(len(strs)):
            # print(''.join(sorted(strs[i])))
            if ''.join(sorted(strs[i])) not in hmap:
                hmap[''.join(sorted(strs[i]))] = [strs[i]]
            else:
                hmap[''.join(sorted(strs[i]))] += [strs[i]]
        ans =[]
        for i in hmap:
            ans.append(hmap[i])
        return ans