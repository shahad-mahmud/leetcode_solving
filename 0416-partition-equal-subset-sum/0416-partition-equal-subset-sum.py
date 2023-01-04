class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2:
            return False
        
        self.n = len(nums)
        self.nums = nums
        self.memo = {}
        
        target = s // 2
        return self.is_possible(target, 0)
        
    def is_possible(self, target, i):
        if target == 0:
            return True
        if target < 0 or i>=self.n:
            return False
        if (i, target) in self.memo:
            return self.memo[(i, target)]
        
        res = self.is_possible(target-self.nums[i], i+1) or self.is_possible(target, i+1)
        
        self.memo[(i, target)] = res
        return res