class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0] * len(nums)
        pre[0] = nums[0]
        
        for i in range(1, len(nums)):
            pre[i] += pre[i-1] + nums[i]
        
        if pre[-1] - pre[0] == 0:
            return 0
        
        for i in range(1, len(nums)):
            left = pre[i-1]
            right = pre[-1] - pre[i]
            
            if left == right:
                return i
        
        return -1