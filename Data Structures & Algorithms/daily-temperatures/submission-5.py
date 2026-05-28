class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []  # 优化：现在只存索引

        for i, temp in enumerate(temperatures):
            # 用 temperatures[stack[-1]] 直接获取栈顶索引对应的温度
            while stack and temp > temperatures[stack[-1]]:
                cur_idx = stack.pop()
                res[cur_idx] = i - cur_idx
            stack.append(i)
                
        return res