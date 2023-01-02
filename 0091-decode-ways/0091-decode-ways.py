class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        self.s, self.n = s, len(s)
        self.memo = {}
        return self.get_count(0)
        
    def get_count(self, i):
        if i>=len(self.s):
            return 1
        if self.s[i] == '0':
            return 0
        if i in self.memo:
            return self.memo[i]
        
        one = self.get_count(i+1)
        two = self.get_count(i+2) if i+2 <= self.n and int(self.s[i:i+2]) <= 26 else 0
        
        self.memo[i] = one+two
        
        return one+two
        