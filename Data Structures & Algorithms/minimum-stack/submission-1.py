class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None: #O(1)
        self.stack.append(val)
        if not self.mstack or self.mstack[-1] >= val:
            self.mstack.append(val)
        
      
    def pop(self) -> None:
        if self.stack[-1] == self.mstack[-1]:
            self.mstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]
