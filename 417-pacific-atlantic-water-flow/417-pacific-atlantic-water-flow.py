class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        self.R = len(heights)
        self.C = len(heights[0])
        self.matrix = heights
        
        pacific = [(0, j) for j in range(self.C)] + [(i, 0) for i in range(1, self.R)]
        atlantic = [(i, self.C-1) for i in range(self.R)] + [(self.R-1, j) for j in range(self.C-1)]
        
        return self.bfs(pacific) & self.bfs(atlantic)
    
    def bfs(self, ocean):
        queue = collections.deque(ocean)
        visited = set(ocean)
        
        while queue:
            r, c = queue.popleft()
            
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < self.R and 0 <= nc < self.C and (nr, nc) not in visited and \
                    self.matrix[nr][nc] >= self.matrix[r][c]:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        
        return visited