class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        res=0
        
        properties = sorted(properties, key=lambda x: (-x[0], x[1]))
        max_=-1
        
        for p in properties:
            if max_>p[1]:
                res+=1
            else:
                max_=p[1]
        
        return res