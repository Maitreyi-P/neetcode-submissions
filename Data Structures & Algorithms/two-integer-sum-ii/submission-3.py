class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        d = defaultdict(int)
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t in d:
                return [d[t], i+1]
            d[numbers[i]] = i+1