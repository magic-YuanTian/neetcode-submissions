class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        res = []
        path = []

        def backtrack(start):

            if sum(path) == target:
                res.append(path[:])
            
            if sum(path) > target and path[-1] > 0:
                return

            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i)
                path.pop()
            
        backtrack(0)
        return res

        