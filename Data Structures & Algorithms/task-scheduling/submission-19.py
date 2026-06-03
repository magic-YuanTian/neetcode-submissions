from collections import defaultdict, Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # counts = list(Counter(tasks).values())
        # max_freq = max(counts)
        # max_num = counts.count(max_freq)

        # res = (max_freq - 1) * (1 + n) + max_num

        # return max(res, len(tasks))

        count = Counter(tasks)

        max_heap = [-freq for freq in count.values()]
        heapq.heapify(max_heap)

        timestamp = 0
        queue = deque()

        while max_heap or queue:
            timestamp += 1

            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq < 0:
                    queue.append([timestamp+n, freq])
            
            while queue and queue[0][0] < timestamp + 1:
                heapq.heappush(max_heap, queue.popleft()[1])


        return timestamp
        