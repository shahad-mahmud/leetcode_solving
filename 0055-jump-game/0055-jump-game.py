class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        
        for i, n in enumerate(nums):
            step = max(step-1, n)
            
            if step <= 0 and i<len(nums)-1:
                return False
        
        return True
        