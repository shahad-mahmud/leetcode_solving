class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res=0
        M=1000000007
        
        for i in range(1, n+1):
            # res = res * 2**(floor(log(i,2)) + 1) + i
            res = ((res%M * (2**(floor(log(i,2)) + 1))%M)%M + i)%M
            # print(f"{i} -- {ceil(log(i,2))} -- {2**ceil(log(i,2))}")
            # print(i, res, log(i,2))
        
        return int(res)