class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev2,prev1,curr = 0,1,1
        for i in range(2,n):
            prev2 = prev1 
            prev1 = curr
            curr = prev2 + prev1
        return curr