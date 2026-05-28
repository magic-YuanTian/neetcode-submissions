class MinStack:

    def __init__(self):
        self.stack = []
        self.cur_min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.cur_min:
            new_min = min(self.cur_min[-1], val)
            self.cur_min.append(new_min)
        else:
            self.cur_min.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.cur_min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.cur_min:
            return self.cur_min[-1]
        else:
            return None
        
