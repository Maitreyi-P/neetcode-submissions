class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hmap = {}
        for i,n in enumerate(nums):
            hmap[target - n] = i
        print(hmap)
        for i,n in enumerate(nums):
            if n in hmap and hmap[n] != i:
                return [i,hmap[n]]