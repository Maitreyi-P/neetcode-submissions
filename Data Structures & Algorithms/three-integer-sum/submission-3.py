class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = sorted(nums)
        print(n)
        for i in range(len(n)):
            target = 0 - (n[i])
            arr = [-target]
            j = i+1
            k = len(nums) -1
            while j<k:
                print(j,k,n[j],n[k],n[i])
                if n[j] + n[k] == target:
                    arr.append(n[j])
                    arr.append(n[k])
                    if arr not in output:
                        output.append(arr)
                    arr=[-target]
                    k -=1
                    j+=1
                elif n[j] + n[k] < target:
                    j+=1
                elif n[j] + n[k] > target:     
                    k -=1
        return output
        