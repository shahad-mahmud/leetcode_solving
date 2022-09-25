class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        
        while r<len(matrix):
            l, h = 0, len(matrix[0])-1
            
            if target<matrix[r][l]:
                break
                
            if target>matrix[r][h]:
                r+=1
                continue
            
            while l<=h:
                m=(l+h)//2
                if matrix[r][m]==target:
                    return True
                
                if target<matrix[r][m]:
                    h=m-1
                else:
                    l=m+1
            
            r+=1
        
        return False
        