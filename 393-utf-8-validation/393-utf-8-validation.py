class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        i=0
        while i < len(data):
            type_=self.get_type(data[i])
            if type_ is None or len(data)-i<type_:
                return False
            
            i+=1
            while type_ and i<len(data):
                if not self.get_type(data[i])==5:
                    return False
                i+=1
                type_-=1
        
        return True
            
    
    def get_type(self, num):
        if num & 128 == 0:
            return 0
        if num & 224 == 192:
            return 1
        if num & 240 == 224:
            return 2
        if num & 248 == 240:
            return 3
        if num & 192 == 128:
            return 5