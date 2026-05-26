class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = {i:1 for i in range(len(nums) + 1)}
        for v in nums:
            del seen[v]

        for key in seen.keys():
            return key

            