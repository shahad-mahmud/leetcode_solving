class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits)-1, -1, -1):
            if carry==0:
                break
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s//10
        
        if carry:
            return [1] + digits
        return digits
        