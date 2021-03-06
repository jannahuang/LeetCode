# 155. ��Сջ
# 20190408

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min == None or self.min > x:
            self.min = x

    def pop(self) -> None:
        popItem = self.stack.pop()
        if len(self.stack) == 0:
            self.min == None
            return popItem
        else:
            if popItem == self.min:
                self.min = self.stack[0]
                for i in self.stack:
                    if self.min > i:
                        self.min = i
        return popItem

    def top(self) -> int:
        if len(self.stack) == 0:
            self.min = None
            return None
        else:
            self.min = self.stack[0]
            for i in self.stack:
                if self.min > i:
                    self.min = i
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()