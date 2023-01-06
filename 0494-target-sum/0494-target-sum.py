class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        
        def dfs(i, s):
            if i==n:
                return 1 if s==target else 0
            if (i, s) in memo:
                return memo[(i, s)]
            
            memo[(i, s)] = dfs(i+1, s+nums[i]) + dfs(i+1, s-nums[i])
            return memo[(i, s)]
        
        return dfs(0, 0)