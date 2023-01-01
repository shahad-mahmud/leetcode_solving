class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = -1
        ords = (0,0)
        
        for i in range(n):
            l, r = i, i
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len = r-l+1
                    ords = (l,r)
                l-=1; r+=1
            
            l, r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len = r-l+1
                    ords = (l, r)
                l-=1; r+=1
        
        l, r = ords
        return s[l:r+1]