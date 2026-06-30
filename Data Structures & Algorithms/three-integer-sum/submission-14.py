class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums = sorted(nums) 

        for i in range(len(nums) - 2):
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue
            ans = [nums[i]]
            target = -1 * nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append(nums[l])
                    ans.append(nums[r])
                    if ans not in res:
                        res.append(ans)
                    ans = [nums[i]]    
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1


        return res

