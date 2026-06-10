class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in range(len(strs)):
            s1 = [0]*26
            # print(''.join(sorted(strs[i])))
            for j in strs[i]:
                s1[ord(j) - ord('a')] += 1
            if tuple(s1) not in hmap:
                hmap[tuple(s1)] = [strs[i]]
            else:
                hmap[tuple(s1)] += [strs[i]]
        ans =[]
        for i in hmap:
            ans.append(hmap[i])
        return ans