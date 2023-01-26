class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left_min, right_max = [prices[0]]*n , [prices[-1]]*n
        
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], prices[i])
            right_max[n-1-i] = max(right_max[n-i], prices[n-1-i])
        
        return max([right_max[i]-left_min[i] for i in range(n)])
        