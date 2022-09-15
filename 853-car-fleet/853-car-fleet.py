class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        info=zip(position, speed)
        info=sorted(info, key=lambda x: x[0], reverse=True)
        time=[(target-p)/s for p, s in info]
        
        stack=[]
        
        for i in range(len(info)):
            stack.append(time[i])
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        