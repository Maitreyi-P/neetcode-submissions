class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hmap = {}
        # for i,n in enumerate(nums):
        #     hmap[target - n] = i
        # for i,n in enumerate(nums):
        #     if n in hmap and hmap[n] != i:
        #         return [i,hmap[n]]


        for i,n in enumerate(nums):
            if n in hmap and hmap[n] != i:
                return [hmap[n],i]
            else:
                hmap[target - n] = i
        