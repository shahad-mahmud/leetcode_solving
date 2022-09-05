class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        right_max=[0 for _ in range(len(prices))]
        
        for i in range(len(prices)-2, -1, -1):
            right_max[i]=max(prices[i+1], right_max[i+1])
        
        for i in range(len(prices)):
            profit=right_max[i]-prices[i]
            
            if profit>max_profit:
                max_profit=profit
        
        return max_profit
        