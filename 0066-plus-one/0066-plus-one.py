class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = []
        i = len(digits) - 1
        digits[i] += 1
        while digits[i] >= 10 and i > 0:
            digits[i - 1] += (digits[i] // 10)
            digits[i] %= 10
            i -= 1
        if digits[0] < 10:
            return digits
        else:
            tmp.append(digits[0] // 10)
            digits[0] %= 10
            tmp += digits
            return tmp
            
