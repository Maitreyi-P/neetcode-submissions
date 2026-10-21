class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}

        for s in strs:
            temp = [0]*26
            for i in s:
                temp[ord(i)-ord('a')] += 1
            if str(temp) in hmap:
                hmap[str(temp)].append(s)
            else:
                hmap[str(temp)] = [s]


        return list(hmap.values())