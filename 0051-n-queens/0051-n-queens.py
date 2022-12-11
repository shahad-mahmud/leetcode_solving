class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solve = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        
        cols, p_diagons, n_diagons = set(), set(), set()
        
        def backtrack(r):
            if r >= n:
                solve_str = [''.join(s) for s in solve]
                res.append(solve_str)
            
            for c in range(n):
                p_diagon = r+c
                n_diagon = r-c
                
                if c not in cols and p_diagon not in p_diagons and n_diagon not in n_diagons:
                    cols.add(c)
                    p_diagons.add(p_diagon)
                    n_diagons.add(n_diagon)
                    
                    solve[r][c]='Q'
                    backtrack(r+1)
                    solve[r][c]='.'
                    
                    cols.remove(c)
                    p_diagons.remove(p_diagon)
                    n_diagons.remove(n_diagon)
                    
        
        backtrack(0)
        return res
        