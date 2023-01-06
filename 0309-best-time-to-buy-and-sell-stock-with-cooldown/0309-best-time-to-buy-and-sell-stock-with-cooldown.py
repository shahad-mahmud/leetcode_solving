class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        
        def solve(i, bought):
            if i>=n:
                return 0
            if (i,bought) in memo:
                return memo[(i,bought)]
            
            if bought:
                memo[(i,bought)] = max(solve(i+2, 0) + prices[i], solve(i+1, 1))
                return memo[(i,bought)]
            memo[(i,bought)] = max(solve(i+1, 1) - prices[i], solve(i+1, 0))
            return memo[(i,bought)]
        
        return solve(0, 0)
        