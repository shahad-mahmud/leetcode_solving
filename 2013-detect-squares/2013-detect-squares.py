class DetectSquares:

    def __init__(self):
        self.points = []
        self.counts = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] += 1
        self.points.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        
        for x, y in self.points:
            if (abs(point[1] - y) != abs(point[0] - x)) or x == point[0] or y == point[1]:
                continue
            res += self.counts[(x, point[1])] * self.counts[(point[0], y)]
        
        return res
            
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)