class Solution:
    memo = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1: return 1
        if min(m,n) <=0: return 0
        if (m,n) in self.memo:
            return self.memo[(m,n)]
        
        res = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        self.memo[(m, n)] = self.memo[(n, m)] = res
        
        return res