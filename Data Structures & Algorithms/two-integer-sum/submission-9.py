class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}
        for i in range(len(nums)):
            hmap[target-nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in hmap and hmap[nums[i]]!= i:
                return [i, hmap[nums[i]]]