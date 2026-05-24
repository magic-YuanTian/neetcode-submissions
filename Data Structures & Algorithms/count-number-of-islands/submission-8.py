from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        res = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":

                    res += 1

                    queue = deque()
                    queue.append((r, c))

                    while queue:
                        
                        cur_r, cur_c = queue.popleft()

                        grid[cur_r][cur_c] = "0"

                        for dir in directions:
                            nr, nc = cur_r + dir[0], cur_c + dir[1]

                            if 0 <= nr < rows and 0 <= nc < cols:
                                if grid[nr][nc] == "1":
                                    queue.append((nr, nc))

        return res