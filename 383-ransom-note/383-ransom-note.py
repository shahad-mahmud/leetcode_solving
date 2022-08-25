class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter={}
        
        for char in magazine:
            if char in counter:
                counter[char]+=1
            else:
                counter[char]=1
        
        for char in ransomNote:
            if char not in counter: return False
            counter[char] -= 1
            if counter[char] < 0: return False
        
        return True