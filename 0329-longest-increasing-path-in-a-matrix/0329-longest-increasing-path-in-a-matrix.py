class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[0]*n for _ in range(m)]
        max_len = 0
        
        def dfs(i, j):
            if (
                i >= m
                or j >= n
                or min(i,j) < 0
            ):
                return 0
            
            if memo[i][j] > 0:
                return memo[i][j]
            
            length = 1
            if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                length = max(length, 1 + dfs(i-1, j))
            if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                length = max(length, 1 + dfs(i, j-1))
            if i+1 < m and matrix[i+1][j] > matrix[i][j]:
                length = max(length, 1 + dfs(i+1, j))
            if j+1 < n and matrix[i][j+1] > matrix[i][j]:
                length = max(length, 1 + dfs(i, j+1))
            
            memo[i][j] = length
            return length
        
        for i in range(m):
            for j in range(n):
                length = dfs(i,j)
                if length > max_len:
                    max_len = length
        return max_len
        