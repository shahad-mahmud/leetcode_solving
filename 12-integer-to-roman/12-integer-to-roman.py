class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        
        result += 'M' * (num // 1000)
        num %= 1000

        result += 'CM' * (num // 900)
        num %= 900

        result += 'D' * (num // 500)
        num %= 500

        result += 'CD' * (num // 400)
        num %= 400

        result += 'C' * (num // 100)
        num %= 100

        result += 'XC' * (num // 90)
        num %= 90

        result += 'L' * (num // 50)
        num %= 50

        result += 'XL' * (num // 40)
        num %= 40

        result += 'X' * (num // 10)
        num %= 10

        result += 'IX' * (num // 9)
        num %= 9

        result += 'V' * (num // 5)
        num %= 5

        result += 'IV' * (num // 4)
        num %= 4

        result += 'I' * num

        return result 