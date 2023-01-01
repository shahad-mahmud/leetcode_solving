class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        self.nums = nums
        
        return max(self.get_max(0, n-1), self.get_max(1, n))
    
    def get_max(self, s, e):
        r1, r2 = 0, 0
        
        for i in range(s, e):
            t = max(r1+self.nums[i], r2)
            r1=r2
            r2=t
        return r2