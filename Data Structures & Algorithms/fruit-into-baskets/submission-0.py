class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        freqMap = defaultdict(int)

        l = 0
        total = 0
        res = 0

        for r in range(len(fruits)):
            freqMap[fruits[r]] += 1
            total += 1

            while len(freqMap) > 2:
                f = fruits[l]
                freqMap[f] -= 1
                total -= 1
                l+=1
                
                if freqMap[f] == 0:
                    freqMap.pop(f)

            res = max(res, total)

        return res
            

            
        
                
            