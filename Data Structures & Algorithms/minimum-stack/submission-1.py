class MinStack:

    def __init__(self):
        self.stack = []
        self.minIndex = 0
        self.prevMin = {0: None}

    def push(self, val: int) -> None:
        index = len(self.stack)

        if self.stack and val < self.stack[self.minIndex]:
            self.prevMin[index] = self.minIndex
            self.minIndex = index

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        index = len(self.stack)

        if index == self.minIndex:
            if self.prevMin[index] is not None:
                self.minIndex = self.prevMin[index]


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.minIndex]
        
