from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)

        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                cur_len = 1
                while cur + 1 in num_set:
                    cur += 1
                    cur_len += 1
                longest = max(longest, cur_len)
            
        
        return longest