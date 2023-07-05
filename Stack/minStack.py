# Using python built in methods uses more time and resource -> 573ms
# This solution wins in the memory consumption, beating almost 90%
class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        return self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return min(self.items)



# Optimal Solution -> 76ms
# Due to using a new memory, this uses more space.
class MinStack:

    def __init__(self):
        self.items = []
        self.minNums = []

    def push(self, val: int) -> None:
        self.items.append(val)
        
        if self.minNums:
            val = min(val, self.minNums[-1])
            return self.minNums.append(val)
        else:
            return self.minNums.append(val)
            

    def pop(self) -> None:
        return self.items.pop(), self.minNums.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minNums[-1]
    
stackObj = MinStack()

stackObj.push(-1)
stackObj.push(0)
stackObj.push(5)

print(stackObj.top())
print(stackObj.getMin())
