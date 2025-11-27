class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # S: P(i) : "best value for subarray that ends at i"
        # R: P(i) = max(a[i], P(i-1)+ a[i]) # extend the previous subarray or start a new subarray.
        # T: P(i) -> P(i-1), reverse topological order: increasing i.
        # B: P(0) = a[0]
        # O: max(P(i))
        memo = [float('inf') for i in range(len(nums))]
        memo[0] = nums[0]
        for i in range(1,len(nums)):
            memo[i] = max(nums[i], memo[i-1]+nums[i])
        return max(memo)   