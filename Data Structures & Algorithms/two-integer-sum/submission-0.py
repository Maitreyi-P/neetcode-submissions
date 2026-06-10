class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {} #hashmap to have value:index
        for i in range(len(nums)):
            if target - nums[i] in hmap: #checking if difference is a key in hmap
                return [hmap[target - nums[i]], i]
            hmap[nums[i]] = i #if diff not a key, add the value and index
        return


        