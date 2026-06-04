class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        val1 = 0
        for s in num1:
            val1 = val1 * 10 + int(s)
        val2 = 0
        for s in num2:
            val2 = val2 * 10 + int(s)
        
        return str(val1 * val2)