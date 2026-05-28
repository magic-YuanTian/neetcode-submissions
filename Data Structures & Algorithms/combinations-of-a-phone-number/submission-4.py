class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = []

        def dfs(path, i):
            nonlocal phone_map, res

            if i == len(digits):
                res.append(path)
                return
            
            num = digits[i]

            if num in digits:
                for ch in phone_map[num]:
                    dfs(path + ch, i + 1)


        dfs('', 0)

        return res
            

