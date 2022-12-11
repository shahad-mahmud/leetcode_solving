class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        self.count=0
        visited = set()
        m,n = len(grid), len(grid[0])
        
        def dfs(i,j):
            if min(i,j)<0 or i>=m or j>=n or grid[i][j]==0:
                if self.count>self.max_area:
                    self.max_area = self.count
                return
            
            self.count+=1
            grid[i][j]=0
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    self.count=0
                    dfs(i,j)
        
        return self.max_area
            