arr = [3,4,6,2]   
n = 6

# brute force

for i in arr:
    for j in arr:
        if(i+j==n):
            if(i==j):
                pass
            else:
                print([i,j])

# This is a bad solution with complexity O(n^2); Adding more steps would make it more inefficient.