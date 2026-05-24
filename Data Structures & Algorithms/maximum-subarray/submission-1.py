class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        left = 0

        res = float('-inf')

        cur = 0

        for right in range(len(nums)):
            
            cur += nums[right]
            res = max(res, cur)

            if cur <= 0:
                left = right
                cur = 0

        return res
                