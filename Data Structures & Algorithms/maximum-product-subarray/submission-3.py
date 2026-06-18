class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        dp = [1] + nums
        min_dp = [1] + nums
        n = len(dp)

        maxpr = -float('inf')

        for i in range(1, n):
            min_dp[i] = min(dp[i],nums[i-1] * dp[i-1], nums[i-1] * min_dp[i-1])
            dp[i] = max(dp[i],nums[i-1] * dp[i-1], nums[i-1] * min_dp[i-1])


        return max(dp[1:])

