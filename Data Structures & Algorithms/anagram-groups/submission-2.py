class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d= defaultdict(list)
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)- 97]+=1
            if str(count) in d:
                d[str(count)].append(s)
            else:
                d[str(count)] = [s]

        return (list(d.values()))

        