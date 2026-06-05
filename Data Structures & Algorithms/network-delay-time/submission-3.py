from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        received = [float('inf')] * n

        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append([v, t])

        queue = deque()
        queue.append([k, 0])
        received[k-1] = 0

        while queue:
            node, pre_t = queue.popleft()
            for target_node, transit_t in graph[node]:
                if received[target_node-1] > pre_t + transit_t:
                    received[target_node-1] = pre_t + transit_t
                    queue.append([target_node, received[target_node-1]])
        

        res = max(received)

        if res == float('inf'):
            return -1
        else:
            return res

