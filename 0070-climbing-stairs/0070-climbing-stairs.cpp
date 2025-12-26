class Solution {
public:
    int climbStairs(int n) {
            /*
    - S : DP(i) : number of ways to climb n steps 
    - R : DP(i) = DP(i-2) + DP(i-1)
    - T : DP(i-2) -> DP(i) <- DP(i-1) : increansing i
    - B : DP(0) = 1 , DP(1) = 1
    - O : DP(n-1)
    */
 
    vector<int> dp(n+1,0);
    dp[0] = 1;
    dp[1] = 1;
    for (int i=2; i<n+1; i++){
        dp[i] = dp[i-2] + dp[i-1];
    };
    return dp[n];
};
};