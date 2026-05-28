class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, target):

            if len(target) == 0:
                return True
            
            if target[0] == board[r][c] and len(target) == 1:
                return True

            if target[0] != board[r][c]:
                return False

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            temp = board[r][c]
            board[r][c] = '#'

            res = False
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if dfs(new_r, new_c, target[1:]):
                        res = True
                        break
                
            board[r][c] = temp
            
            return res

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, word):
                    return True

        return False

