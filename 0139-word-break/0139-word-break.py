class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.n, self.s = len(s), s
        self.dict = set(wordDict)
        self.memo = {}
        
        return self.is_possible(0)
        
    def is_possible(self, i):
        if i==self.n:
            return True
        if i in self.memo:
            return self.memo[i]
        
        for j in range(i, self.n):
            if self.s[i:j+1] in self.dict:
                if self.is_possible(j+1):
                    self.memo[i] = True
                    return True
        
        self.memo[i] = False
        return False
        