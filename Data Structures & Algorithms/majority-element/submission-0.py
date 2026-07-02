class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maj = (len(nums)//2) + 1

        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for k,v in count.items():
            if v >= maj:
                return k
