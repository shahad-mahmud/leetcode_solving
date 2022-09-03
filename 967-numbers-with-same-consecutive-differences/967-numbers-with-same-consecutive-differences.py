class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.res=[]
        self.k=k
        self.n=n
        
        for i in range(1, 10):
            self.add_next_num(i)
        
        return self.res
        
    def add_next_num(self, current_num):
        if len(str(current_num))==self.n: return current_num
        
        if current_num%10 - self.k >=0:
            temp = self.add_next_num(current_num*10 + (current_num%10 - self.k))
            if temp: self.res.append(temp)
        
        if self.k!=0 and current_num%10 + self.k <=9:
            temp = self.add_next_num(current_num*10 + (current_num%10 + self.k))
            if temp: self.res.append(temp)
        