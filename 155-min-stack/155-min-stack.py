class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append({
                'current' : value,
                'minimum' : value,
            })
        else:
            self.stack.append({
                    'current' : value,
                    'minimum' : min(value,self.stack[-1]['minimum']),
                })

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]['current']

    def getMin(self) -> int:
        return self.stack[-1]['minimum']


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()