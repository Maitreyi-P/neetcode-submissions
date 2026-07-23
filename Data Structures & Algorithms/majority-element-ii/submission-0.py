class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        maj = len(nums)//3
        res = []
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        for n in count:
            if count[n] > maj:
                res.append(n)

        return res