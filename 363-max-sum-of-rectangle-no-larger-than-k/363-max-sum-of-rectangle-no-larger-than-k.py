class Solution:    
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m=len(matrix)
        n=len(matrix[0])
        res=float('-inf')
        
        prefix_sum=[[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix_sum[i][j]=matrix[i-1][j-1]+prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]
        
        for i1 in range(m):
            for i2 in range(i1, m):
                row_sums=[]
                
                for j in range(n):
                    ract_sum=prefix_sum[i2+1][j+1]-prefix_sum[i2+1][0]-prefix_sum[i1][j+1]+prefix_sum[i1][0]
                    comp=ract_sum-k
                    
                    if ract_sum<=k:
                        res=max(res,ract_sum)
                        
                    i = bisect.bisect_left(row_sums, comp)    
                    if row_sums and i < len(row_sums):
                        if ract_sum - row_sums[i] <= k:
                            res = max(res, ract_sum - row_sums[i])
                    
                    bisect.insort(row_sums, ract_sum)
        
        return res