class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        number = x
        if number<0:
            return False
        while number>0:
            units = number % 10
            reverse = (reverse * 10) + units
            number = (number - units)/10
        return x == int(reverse)