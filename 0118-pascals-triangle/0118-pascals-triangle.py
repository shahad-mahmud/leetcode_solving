class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        for i in range(1, numRows+1):
            temp = []
            for j in range(i):
                if j==0 or j==i-1:
                    temp.append(1)
                else:
                    temp.append(res[i-2][j-1]+res[i-2][j])
            res.append(temp)
        
        return res
        