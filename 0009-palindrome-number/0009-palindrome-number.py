class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        m = int(len(x)/2)
        for i in range(m):
            if x[i] != x[-1-i]:
                return False
        return True