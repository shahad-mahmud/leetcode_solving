class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_chars = set()
        max_len = 0
        l, r = 0, 0
        
        while r<len(s):
            if s[r] in current_chars:
                max_len = max(r-l, max_len)
                
                while s[r] in current_chars:
                    current_chars.remove(s[l])
                    l+=1
            current_chars.add(s[r])
            r+=1
        max_len = max(r-l, max_len)
        
        return max_len
        