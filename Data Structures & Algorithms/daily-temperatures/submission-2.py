class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        
        # monotonic stack, values decrease
        # (idx, temp)
        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and temp > stack[-1][1]:
                cur_idx, cur_temp = stack.pop()
                res[cur_idx] = i - cur_idx
            stack.append((i, temp))
                

        return res