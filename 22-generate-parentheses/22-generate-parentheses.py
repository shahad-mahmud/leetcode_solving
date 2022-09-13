class Solution:    
    def generateParenthesis(self, n: int, s=[]) -> List[str]:
        return self.gen("(", n-1, ["("])
    
    def gen(self, cur, n, s):
        if n<=0 and len(s)==0:
            return [cur]
        
        res=[]
        if n>0:
            res+=self.gen(cur+"(", n-1, s+["("])
        if s:
            res+=self.gen(cur+")", n, s[:-1])
        
        return res