def dailyTemp(temp):
    tempStack = []  # [(index, value)]
    outStack = [0] * len(temp)
    
    for i,j in enumerate(temp):
        while tempStack and j > tempStack[-1][1]:
            stack_index , stack_temp = tempStack.pop()
            outStack[stack_index] = i-stack_index
        tempStack.append((i,j))
    return outStack
        
        
        
temp = [68,72,73,69,81,72]
print(dailyTemp(temp))