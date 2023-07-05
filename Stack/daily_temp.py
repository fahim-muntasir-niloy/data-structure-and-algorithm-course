def dailyTemp(temp):
    tempStack = []
    outStack = []
    
    for i,j in enumerate(temp):
        if tempStack:
            if tempStack[-1]<j:
                # tempStack.pop()
                tempStack.append(i)
            
        else:
            tempStack.append(i)
            
    return tempStack
        
        
        
temp = [68,72,73,69,81,72]
print(dailyTemp(temp))