class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        res, combs = [], []
        
        def backtrack(i):
            if i>=len(digits):
                res.append(''.join(combs))
                return
            
            for letter in digit_map[digits[i]]:
                combs.append(letter)
                backtrack(i+1)
                combs.pop()
        
        backtrack(0)
        return res
        