class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        memo = {}
        
        def solve(i, j):
            if i >= l1 or j>= l2:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i] == text2[j]:
                memo[(i,j)] = solve(i+1, j+1) + 1
                return memo[(i,j)]
            
            memo[(i,j)] = max(solve(i+1, j), solve(i, j+1))
            return memo[(i,j)]
        
        return solve(0, 0)
        