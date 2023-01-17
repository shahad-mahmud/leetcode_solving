class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1+n2)
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(n1):
            for j in range(n2):
                mul = int(num1[i]) * int(num2[j])
                
                res[i+j] += mul
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10
        
        res, i = res[::-1], 0
        while i<len(res) and res[i]==0:
            i+=1
        
        res = map(str, res[i:])
        return "".join(res)
            