# Two Sum II - Input Array Is Sorted
# The catch here is the input array is 1-index

# Fun part is if you can solve TwoSum, You can already do this one.

inp_arr = [2,7,11,13]
target = 20
empty_dict = {}

def twosum2(arr, target):
    for i,j in enumerate(arr):
        diff = target - j
        
        if diff in empty_dict:
            return (empty_dict[diff]+1, i+1)
        
        empty_dict[j] = i
    
# print(twosum2(inp_arr,target))


# The two pointer approach
# This is useful due to the sorted nature of the array.

def twosum2pointer(arr,target):
    s, e = 0, len(arr)-1
    
    while s!=e:
        if arr[s] + arr[e] < target:
            s += 1
        elif arr[s] + arr[e] > target:
            e -= 1
        else:
            return (s+1, e+1)
    

print(twosum2pointer(inp_arr, target))
    