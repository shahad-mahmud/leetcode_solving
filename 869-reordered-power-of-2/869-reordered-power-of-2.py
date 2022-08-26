class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digit_count = Counter(str(n))
        
        for i in range(30):
            power = 1 << i
            
            if digit_count == Counter(str(power)):
                return True
        
        return False