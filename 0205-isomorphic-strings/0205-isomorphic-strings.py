class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        
        m = {}
        for a, b in zip(s, t):
            if a not in m:
                m[a] = b
            
            a = m[a]
            if a!= b:
                return False
        
        return True
        