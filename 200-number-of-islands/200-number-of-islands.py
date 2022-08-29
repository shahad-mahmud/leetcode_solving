class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        n_ilands=0
        
        def change(i, j):
            grid[i][j]="-1"
                
                
            if i>0 and grid[i-1][j]=="1": change(i-1,j)
            if j>0 and grid[i][j-1]=="1": change(i,j-1)
            if i<m-1 and grid[i+1][j]=="1": change(i+1,j)
            if j<n-1 and grid[i][j+1]=="1": change(i,j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    n_ilands+=1
                    change(i,j)
        
        return n_ilands
                
        