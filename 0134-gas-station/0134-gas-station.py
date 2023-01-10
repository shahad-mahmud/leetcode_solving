class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start, total = 0, 0
        
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g-c
            
            if total < 0:
                total=0
                start=i+1
        
        return start
                
        