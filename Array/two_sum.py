arr = [3,4,6,2]   
n = 8

empty_set = {}

def twoSum(arr, n):
    for i,j in enumerate(arr):
        left = n-j
        if left in empty_set:
            return [empty_set[left], i]
        empty_set[j] = i
    
print(twoSum(arr,n))