class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if not k: return 0
        
        profit = [0 for _ in range(k+1)]        
        cost = [float('inf') for _ in range(k+1)]
        
        for price in prices:
            for i in range(k):
                cost[i+1] = min(cost[i+1],price-profit[i])
                profit[i+1] = max(profit[i+1], price-cost[i+1])
        
        return profit[k]