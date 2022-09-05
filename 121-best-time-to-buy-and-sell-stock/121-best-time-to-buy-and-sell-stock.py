class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        lp, rp=0, 1
        
        while rp<len(prices):             
            profit=prices[rp]-prices[lp]
            
            if profit>max_profit:
                max_profit=profit
            
            if prices[lp]>prices[rp]:
                lp=rp
            rp+=1
        
        return max_profit
        