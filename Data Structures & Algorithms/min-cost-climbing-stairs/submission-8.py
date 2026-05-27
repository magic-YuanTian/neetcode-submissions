class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # [1,2,1]

        n = len(cost)

        if n < 2:
            return 0

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i], dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        print(dp)

        return dp[n]