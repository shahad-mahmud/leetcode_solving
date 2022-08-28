class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        
        for i in range(n):
            temp=[]
            j=0 
            k=i
            
            while j<m and k<n:
                temp.append(mat[j][k])
                j+=1
                k+=1
            
            temp=list(sorted(temp))
            
            j=0 
            k=i
            for v in temp:
                mat[j][k]=v
                j+=1
                k+=1
        
        for i in range(1, m):
            temp=[]
            j=i
            k=0
            
            while j<m and k<n:
                temp.append(mat[j][k])
                j+=1
                k+=1
            
            temp=list(sorted(temp))
            
            j=i
            k=0
            for v in temp:
                mat[j][k]=v
                j+=1
                k+=1
        
        return mat
        