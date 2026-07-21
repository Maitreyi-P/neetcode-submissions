class Solution:
    def isHappy(self, n: int) -> bool:

        def squaresum(num):
            res = 0
            s = str(num)
            for c in s:
                print(int(c) ** 2)
                res += (int(c) ** 2)

            return res


        slow = n
        fast = squaresum(n)

        while slow != fast:
            fast = squaresum(fast)
            fast = squaresum(fast)
            slow = squaresum(slow)

        if fast == 1:
            return True
        return False