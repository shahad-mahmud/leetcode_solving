class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m = 0

        gaps = defaultdict(int)

        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                gaps[pos] += 1

                m = max(m, gaps[pos])
        
        return len(wall) - m
        