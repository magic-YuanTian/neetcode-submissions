import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1 = - heapq.heappop(heap)
            s2 = - heapq.heappop(heap)
            remain = - abs(s1 - s2)
            heapq.heappush(heap, remain)
        
        if heap:
            res = - heap[0]
        else:
            res = 0
        return res

