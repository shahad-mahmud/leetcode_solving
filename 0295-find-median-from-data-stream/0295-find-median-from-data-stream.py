class MedianFinder:

    def __init__(self):
        self.min, self.max = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min, -num)
        
        if self.min and self.max and -self.min[0] > self.max[0]:
            t = heapq.heappop(self.min)
            heapq.heappush(self.max, -t)
        
        if abs(len(self.min) - len(self.max)) > 1:
            if len(self.min) > len(self.max):
                t = heapq.heappop(self.min)
                heapq.heappush(self.max, -t)
            else:
                t = heapq.heappop(self.max)
                heapq.heappush(self.min, -t)
        

    def findMedian(self) -> float:
        if len(self.min) == len(self.max):
            return (self.max[0]-self.min[0]) / 2
        elif len(self.min) > len(self.max):
            return -self.min[0]
        else:
            return self.max[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()