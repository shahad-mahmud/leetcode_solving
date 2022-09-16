class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m=len(multipliers)
        dp=[[0]*(m+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(i, -1, -1):
                l=nums[j]*multipliers[i] + dp[i+1][j+1]
                r=nums[len(nums)-1-(i-j)]*multipliers[i] + dp[i+1][j]
                dp[i][j]=max(l,r)
        
        
        return dp[0][0]