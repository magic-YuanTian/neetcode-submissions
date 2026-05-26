class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cur_low = float('inf')

        res = 0

        for price in prices:

            res = max(res, price - cur_low)

            cur_low = min(cur_low, price)
        

        return res