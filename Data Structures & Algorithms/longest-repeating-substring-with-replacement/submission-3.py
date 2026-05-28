from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # remain = k + 1

        count = defaultdict(int)

        left = 0
        res = 0


        for right in range(len(s)):

            # update the count
            ch = s[right]
            count[ch] += 1

            # check constraint
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
