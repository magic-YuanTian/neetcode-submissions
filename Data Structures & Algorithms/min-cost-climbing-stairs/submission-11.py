class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # [1,2,1]

        n = len(cost)

        prev1 = 0
        prev2 = 0

        for i in range(2, n + 1):
            cur = min(
                prev1 + cost[i-1],
                prev2 + cost[i-2],
            )
            prev2 = prev1
            prev1 = cur

        return cur

        