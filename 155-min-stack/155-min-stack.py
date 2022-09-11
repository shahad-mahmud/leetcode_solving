class MinStack:

    def __init__(self):
        self._min=deque([float('inf')])
        self.container=deque()
        

    def push(self, val: int) -> None:
        self.container.append(val)
        
        if val <= self._min[-1]:
            self._min.append(val)
        else:
            self._min.append(self._min[-1])
        

    def pop(self) -> None:
        self.container.pop()
        self._min.pop()
        

    def top(self) -> int:
        return self.container[-1]
        

    def getMin(self) -> int:
        return self._min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()