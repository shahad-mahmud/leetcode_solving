class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        
        def solve(amnt, i):
            # print(amnt)
            if amnt == 0:
                return 1
            if amnt < 0:
                return 0
            if i >= n:
                return 0
            if (amnt, i) in memo:
                return memo[(amnt, i)]
            
            memo[(amnt, i)] = solve(amnt-coins[i], i) + solve(amnt, i+1)
            return memo[(amnt, i)]
        
        return solve(amount, 0)