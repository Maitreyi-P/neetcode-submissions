class Solution:
    def isHappy(self, n: int) -> bool:
        
        def squaresum(num):
            res = 0
            s = str(num)
            for c in s:
                print(int(c) ** 2)
                res += (int(c) ** 2)

            return res
       
       
        visit = set()
        while n not in visit:
            visit.add(n)
            n = squaresum(n)
            if n == 1:
                return True
        return False

       