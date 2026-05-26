class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for ch in s:
            if stack:
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                    continue
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                    continue
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
            
            stack.append(ch)

        return len(stack) == 0
            
            