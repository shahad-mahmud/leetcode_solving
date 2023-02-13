class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)
        
        for char in magazine:
            count[char]+=1
        
        for char in ransomNote:
            if not count[char]:
                return False
            
            count[char]-=1
        
        return True
        