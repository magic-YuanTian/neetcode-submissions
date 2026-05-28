from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        res = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    continue

                queue = deque([(r, c)])
                cur_area = 0
                
                while queue:
                    cur_r, cur_c = queue.popleft()
                    if grid[cur_r][cur_c] == 1:
                        cur_area += 1
                        grid[cur_r][cur_c] = 0
                        for dr, dc in directions:
                            new_r, new_c = cur_r + dr, cur_c + dc
                            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                                queue.append((new_r, new_c))

                res = max(res, cur_area)

        return res
                
