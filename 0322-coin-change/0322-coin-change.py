class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.memo = {}
        
        return self.count(amount)
    
    def count(self, amount):
        if amount == 0:
            return 0
        if amount <0:
            return -1
        if amount in self.memo:
            return self.memo[amount]
        
        min_ways = float('inf')
        is_possible = False
        for coin in self.coins:
            t = amount - coin
            
            n_ways = self.count(t)
            if n_ways >= 0 and n_ways < min_ways:
                is_possible = True
                min_ways = n_ways
        
        self.memo[amount] = min_ways + 1 if is_possible else -1
        return self.memo[amount]
                
        