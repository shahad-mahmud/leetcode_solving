class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s  = 0
        m = -1
        zero_in = False
        
        for n in nums:
            if n==0:
                zero_in = True
            s+=n
            if n>m:
                m=n
        
        sum_ = (m*(m+1) // 2)
        if s==sum_:
            if zero_in:
                return m+1
            return 0
        
        return (m*(m+1) // 2) - s