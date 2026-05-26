class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = {n}

        num = n

        while True:
            
            cur = 0
            
            while num // 10 > 0:
                cur += (num % 10) ** 2
                num = num // 10
            
            cur += num ** 2

            if cur == 1:
                return True

            if cur in seen:
                return False
        
            seen.add(cur)

            num = cur

                

