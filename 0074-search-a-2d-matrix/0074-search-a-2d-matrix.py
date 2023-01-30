class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # find row: log(m)
        l, h = 0, m-1
        while l<=h:
            row = (l+h) // 2
            
            if matrix[row][0] <= target <= matrix[row][-1]:
                break
            elif target < matrix[row][0]:
                h = row-1
            else:
                l = row+1
        
        # find col: log(n)
        l, h = 0, n-1
        while l<=h:
            col = (l+h) // 2
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                h = col-1
            else:
                l = col+1
        
        return False
        
        