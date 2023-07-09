def dailyTemp(temp):
    tempStack = []    # (value, position)
    outStack = [0]*len(temp)
    
    for i,j in enumerate(temp):
        while tempStack and j>tempStack[-1][1]:
                idx, val = tempStack.pop()
                outStack[idx] = i-idx
                
        tempStack.append((i,j))
    
            
    return outStack
        
        
        
temp = [73,74,75,71,69,72,76,73]
print(dailyTemp(temp))