class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right, top, bottom = 0, n, 0, n
        nums = list(range(1, n*n + 1))
        matrix = [[None]*n for _ in range(n)]
        i = 0
        
        while left<right and top<bottom and i<n*n:
            for j in range(left, right):
                matrix[top][j] = nums[i]
                i+=1
            top+=1
            
            for j in range(top, bottom):
                matrix[j][right-1] = nums[i]
                i+=1
            right-=1
            
            for j in range(right-1, left-1, -1):
                matrix[bottom-1][j] = nums[i]
                i+=1
            bottom-=1
            
            for j in range(bottom-1, top-1, -1):
                matrix[j][left] = nums[i]
                i+=1
            left+=1
        
        return matrix
        