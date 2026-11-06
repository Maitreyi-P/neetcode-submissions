class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # pass


        maxsum = 0
        currsum = 0

        l = 0
        r = 0

        subarr = set()
        while r < len(nums):
            
            while nums[r] in subarr:
                subarr.remove(nums[l])
                currsum -= nums[l]
                l+=1

            subarr.add(nums[r])
            currsum += nums[r]


            if r-l+1 > k:
                subarr.remove(nums[l])
                currsum -= nums[l]
                l += 1

            if (r-l+1) == k:
                maxsum = max(maxsum, currsum)

            r+=1

            

        return maxsum
