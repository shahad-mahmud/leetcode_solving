class Solution:
    dp=[-1 for _ in range(46)]
    dp[0]=1
    
    def climbStairs(self, n: int) -> int:
        if n<0: return 0        
        if self.dp[n] >=0: return self.dp[n]
        
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
        