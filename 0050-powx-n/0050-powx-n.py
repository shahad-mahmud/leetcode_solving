class Solution:
    def myPow(self, x: float, n: int) -> float:
        n_ = abs(n)
        expo = 1
        while n_:
            if (n_&1):
                expo *= x
            x = x*x
            n_ >>= 1
        
        return expo if n>=0 else 1/expo