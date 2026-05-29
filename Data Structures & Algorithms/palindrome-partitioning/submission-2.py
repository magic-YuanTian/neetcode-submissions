class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        path = []

        def is_palindrome(s):
            return s == s[::-1]


        def backtrack(path, start):

            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start + 1, len(s)+1):
                cur = s[start: end]
                if is_palindrome(cur):
                    path.append(cur)
                    backtrack(path, end)
                    path.pop()
        
        backtrack(path, 0)

        return res
