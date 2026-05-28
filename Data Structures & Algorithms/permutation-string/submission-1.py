from collections import defaultdict, Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0

        window = defaultdict(int)
        s1_count = Counter(s1)
        target_len = len(s1)

        for right in range(len(s2)):
            ch = s2[right]
            window[ch] += 1
            while s1_count[ch] < window[ch]:
                window[s2[left]] -= 1
                left += 1
            
            if right - left + 1 == target_len:
                return True
        
        return False

