class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # M[x] = min number of coins to make amount x
        # Initialize: M(0) = 0, others = +inf (unreachable)
        # subproblems: M(x): "min coin change for amout x "
        # relate:  M(i) = min(M(i-c)+1, for all c in coins)
        # Topological order: [M(0),M(1),.....,M(amount)]
        # Base case: M(0) = 0 , M(x) = +inf if x<0
        # Original problem: M(amout)
        M = [float('inf')] * (amount + 1)
        M[0] = 0
        if amount == 0:
            return M[0]
        for i in range(1,amount+1):
            for c in coins:
                if i-c < 0:
                    continue
                M[i] = min(M[i], M[i-c]+1)
        if M[amount] == inf:
            return -1
        return M[amount]