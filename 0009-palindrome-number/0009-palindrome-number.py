class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        revx = x[::-1]
        return x == revx