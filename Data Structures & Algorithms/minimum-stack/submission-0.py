class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            min_val = min(val, self.minstack[-1])
            self.minstack.append(min_val)
        else:
            self.minstack.append(val)


    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
