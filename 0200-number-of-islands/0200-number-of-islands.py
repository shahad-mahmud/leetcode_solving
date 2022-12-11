class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def dfs(i,j):
            if min(i,j)<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
                return
            
            grid[i][j]='0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=='1':
                    count += 1
                    dfs(r,c)
        
        return count
            
        