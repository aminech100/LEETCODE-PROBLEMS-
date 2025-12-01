class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
    # Subproblems: L(i,j): length of LCS of s1[0:i] and s2[0:j]
    # Relation: 
    #   if s1[i-1] == s2[j-1]: L(i,j) = 1 + L(i-1, j-1)
    #   else: L(i,j) = max(L(i-1, j), L(i, j-1))
    # Topological order: increasing i and j
    # Base cases: L(0,j) = 0 and L(i,0) = 0
    # Original problem: L(len(s1), len(s2))

        memo = [[0] * (len(s2)+1) for _ in range(0,len(s1)+1)]
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if s1[i-1] == s2[j-1] : 
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j],memo[i][j-1])

        return memo[len(s1)][len(s2)]