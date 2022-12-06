class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bfs(i,j, word_i, visited):
            # print(i,j,word_i)
            
            if i>=len(board) or j>=len(board[0]) or i<0 or j<0 or word_i>=len(word):
                return False
            if board[i][j] != word[word_i]:
                return False
            if word_i == len(word)-1: return True
            
            # visited.add((i,j))
            res = False
            if (i+1,j) not in visited:
                res = res or bfs(i+1, j, word_i+1, visited.union({(i,j)}))
            if (i-1,j) not in visited:
                res = res or bfs(i-1, j, word_i+1, visited.union({(i,j)}))
            if (i,j+1) not in visited:
                res = res or bfs(i, j+1, word_i+1, visited.union({(i,j)}))
            if (i,j-1) not in visited:
                res = res or bfs(i, j-1, word_i+1, visited.union({(i,j)}))
            
            return res
        
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if bfs(r,c, 0, set()):
                        return True
        
        return False
        