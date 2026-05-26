class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = {}


        for v in nums:
            if v in seen:
                return True
            seen[v] = 1
        
        return False