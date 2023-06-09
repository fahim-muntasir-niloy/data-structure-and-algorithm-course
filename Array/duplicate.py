# a = [21,1,2,2,2,2,2,2,2] 
a = [2,8,22,1,4,22]


# This also works taking hash_set as empty list and appending items. But it is slower than adding to set.


def duplicate(arr):
   hash_set = set()     # Variable should be function scope rather than global scope.
   for j in arr:
      if j in hash_set:
         return True
      hash_set.add(j)
   return False
      

print(duplicate(a))
print(len(a))

