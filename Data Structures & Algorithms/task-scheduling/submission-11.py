from collections import defaultdict, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        max_freq = max(counts)
        max_num = counts.count(max_freq)

        res = (max_freq - 1) * (1 + n) + max_num


        return max(res, len(tasks))