class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        
        while b:
            temp = ((a&b) << 1) & MASK
            a = (a^b) & MASK
            b = temp
        
        return a if a <= MAX else ~(a^MASK)
        