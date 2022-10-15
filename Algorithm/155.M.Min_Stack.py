class MinStack:

    def __init__(self):
        self.val =[]

    def push(self, val: int) -> None:
        self.val.append(val)

    def pop(self) -> None:
        return self.val.pop()
        

    def top(self) -> int:
        return self.val[-1]
        

    def getMin(self) -> int:
        return min(self.val)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()