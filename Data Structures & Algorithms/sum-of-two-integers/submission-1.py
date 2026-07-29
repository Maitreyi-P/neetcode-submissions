class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b:
            temp = a
            a = (a ^ b) & MASK
            b = ((temp & b) << 1) & MASK

        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)    
        
