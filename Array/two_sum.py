arr = [3,4,7,1,2]   
n = 9

# bad brute force

# for i in arr:
#     for j in arr:
#         if(i+j==n):
#             if(i==j):
#                 pass
#             else:
#                 print([i,j])

# This is a bad solution with complexity O(n^2); 
# Adding more steps would make it more inefficient.

# plus minus
def twosum(arr, n):
    hash_map = {}       # value : Index
    for i,j in enumerate(arr):
        diff = n-j
        if diff in hash_map:
            return (hash_map[diff], i)
        hash_map[j] = i

print(twosum(arr,n))