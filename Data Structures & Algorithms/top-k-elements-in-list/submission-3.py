class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
        s = sorted(hmap.items(), key=lambda i:i[1], reverse=True)
        print(s)
        ans = []
        for i in range(k):
            ans.append(s[i][0])
        return ans