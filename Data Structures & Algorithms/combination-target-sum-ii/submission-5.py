class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        path = []

        def backtrack(start, target_remain):
            if target_remain == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                
                if candidates[i] > target_remain:
                    break
                
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, target_remain - candidates[i])
                path.pop()
        

        backtrack(0, target)
        return res