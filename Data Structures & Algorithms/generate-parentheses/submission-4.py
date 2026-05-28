class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        left_num, right_num = 0, 0
        path = ""
        res = []

        def backtrack():
            nonlocal left_num, right_num, res, path

            if left_num == n and right_num == n:
                res.append(path)

            if left_num < n:
                path += "("
                left_num += 1
                backtrack()
                left_num -= 1
                path = path[:-1]
            
            if right_num < left_num:
                path += ")"
                right_num += 1
                backtrack()
                right_num -= 1
                path = path[:-1]

        
        backtrack()

        return res