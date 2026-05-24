from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = defaultdict(int)

        left, right = 0, 0

        res = ""
        max_len = 0

        while right < len(s):
            
            cur = s[right]
            window[cur] += 1
            right += 1

            while cur in window.keys() and window[cur] > 1:
                window[s[left]] -= 1
                left += 1

            if right - left > max_len:
                res = s[left: right]
                max_len = right - left

            

        return max_len