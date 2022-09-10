class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost=cost
        self.dp=[-1 for _ in range(len(cost))]
        self.length=len(cost)
        
        return min(self.min_cost(0), self.min_cost(1))
    
    def min_cost(self, current_position):
        if current_position >= self.length:
            return 0
        
        if self.dp[current_position] > -1:
            return self.dp[current_position]
        
        self.dp[current_position] = self.cost[current_position] + min(self.min_cost(current_position+1), self.min_cost(current_position+2))
        
        return self.dp[current_position]