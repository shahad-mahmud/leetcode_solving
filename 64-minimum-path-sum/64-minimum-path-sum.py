class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp=[[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.grid=grid
        
        return self.min_path(0,0)
    
    def min_path(self, i, j):
        if i==len(self.grid)-1 and j==len(self.grid[0])-1:
            return self.grid[i][j]
        if i>=len(self.grid) or j>=len(self.grid[0]):
            return float('inf')
        
        if self.dp[i][j]>=0: return self.dp[i][j]
        
        m = self.grid[i][j] + self.min_path(i+1, j)
        m = min(m, self.grid[i][j] + self.min_path(i, j+1))
        
        self.dp[i][j]=m
        return m