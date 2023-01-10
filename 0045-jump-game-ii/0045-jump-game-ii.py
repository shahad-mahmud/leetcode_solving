class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums)-1
        memo = {}
        
        def solve(i):
            if i>=target:
                return 1
            if i in memo:
                return memo[i]
            
            res = 999999
            for j in range(nums[i]):
                res = min(res, solve(i+j+1))
            
            memo[i] = 1+res
            return memo[i]
        
        return solve(0)-1
        