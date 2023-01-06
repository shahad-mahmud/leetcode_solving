class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i1, i2, i3 = len(s1), len(s2), len(s3)
        if i1+i2 != i3:
            return False
        
        memo = {}
        
        def solve(i, j):
            # print(r, len(r), len(s3))
            if i==i1 and j==i2:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            
            a, b = False, False
            if i < i1 and s1[i] == s3[i+j]:
                a = solve(i+1, j)
            if j < i2 and s2[j] == s3[i+j]:
                b = solve(i, j+1)
            
            memo[(i,j)] = a or b
            return a or b
        
        return solve(0,0)