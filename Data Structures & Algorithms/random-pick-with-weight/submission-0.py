class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)
        self.prefixsum = [0]
        for weight in w:
            self.prefixsum.append(self.prefixsum[-1]+ weight)

    def pickIndex(self) -> int:
        target = self.total * random.random()
        l,r = 0, len(self.prefixsum)
        while l < r:
            m = l + (r-l)//2
            if self.prefixsum[m] == target:
                return m
            elif self.prefixsum[m] < target:
                l = m+1
            else:
                r = m

        return l - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()