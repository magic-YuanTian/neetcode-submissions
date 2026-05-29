from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        heap = []

        for v, freq in count.items():
            heapq.heappush(heap, (freq, v))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [v for freq, v in heap]


