class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, 0
        turn = 0
        res = []
        
        for _ in range(rows*cols):
            res.append(matrix[r][c])
            
            if turn == 0:
                c+=1
                
                if c==cols:
                    turn = 1
                    cols -= 1
                    c-=1
                    r+=1
            elif turn == 1:
                r+=1
                
                if r==rows:
                    turn = 2
                    rows -= 1
                    r -= 1
                    c = cols - 1
            elif turn == 2:
                c -= 1
                
                if c == len(matrix[0]) - cols - 2:
                    turn = 3
                    r -= 1
                    c += 1
                    # print(2, r, c)
            elif turn == 3:
                r-=1
                
                if r == len(matrix) - rows - 1:
                    # print('KKK', r, c)
                    turn = 0
                    c += 1
                    r += 1
                    # print(3, r, c)
        
        return res
                    
                    
            
        