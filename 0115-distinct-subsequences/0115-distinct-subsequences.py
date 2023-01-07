class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        memo = {}
        
        def solve(i, ts):
            if ts == t:
                return 1
            if i >= n or len(ts) >= m:
                return 0
            if not t.startswith(ts):
                return 0
            if (i, ts) in memo:
                return memo[(i,ts)]
            
            memo[(i,ts)] = solve(i+1, ts) + solve(i+1, ts+s[i])
            return memo[(i,ts)]
        
        return solve(0,"")