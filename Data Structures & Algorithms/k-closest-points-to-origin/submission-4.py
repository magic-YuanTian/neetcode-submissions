import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for pt in points:
            
            dist = pt[0] ** 2 + pt[1] ** 2

            heapq.heappush(heap, [-dist, pt])

            while len(heap) > k:
                heapq.heappop(heap)

        return [pt for dist, pt in heap]


        