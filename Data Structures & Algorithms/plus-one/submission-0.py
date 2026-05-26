class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = 0
        for digit in digits:
            val = val * 10 + digit
        
        val += 1

        res = []

        while val // 10 > 0:
            res.append(val % 10)
            val = val // 10
        res.append(val)
        res.reverse()
        return res
