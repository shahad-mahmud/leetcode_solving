class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, parts = [], []
        self.s = s
        
        def dfs(i):
            if i >= len(s):
                res.append(parts.copy())
            
            for j in range(i, len(s)):
                if self.is_palindrome(i, j):
                    parts.append(s[i:j+1])
                    dfs(j+1)
                    parts.pop()
        
        dfs(0)
        return res
    
    def is_palindrome(self, l, h):
        while l<h:
            if self.s[l] != self.s[h]:
                return False
            
            l+=1
            h-=1
        return True
        