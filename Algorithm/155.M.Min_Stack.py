#첫번째 풀이  2672ms 5% faster 

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






# 145ms 22.92 % 18mb faster 푸는 방법을 잘 몰랐던듯..

class MinStack:

    def __init__(self):
        self.val =[]
        self.min_stack =[]

    def push(self, val: int) -> None:
        self.val.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))

    def pop(self) -> None:
        self.min_stack.pop()
        return self.val.pop()
        

    def top(self) -> int:
        return self.val[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()