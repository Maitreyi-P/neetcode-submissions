class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d= {}
        res = []

        for i in range(len(nums)):
            d[target - nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in d:
                if i == d[nums[i]]:
                    continue
                return[i,d[nums[i]]]
        return res
                
            