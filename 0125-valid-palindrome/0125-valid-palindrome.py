class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if 97 <= ord(c.lower()) <= 122 or 48 <= ord(c.lower()) <= 57]
        
        n = len(chars)
        if n<=1:
            return True
        
        l, r = 0, n-1
        while l<=r:
            if chars[l] != chars[r]:
                return False
            
            l+=1
            r-=1
        
        return True
        