class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res = x

        if n == 0:
            return 1

        if n > 0:
            while n > 1:
                res = res * x
                n -=1
        
            return res
        
        if n < 0:
            while n < -1:
                res = res * x
                n += 1
            return (1 / res)

        