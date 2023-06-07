# a = [21,1,2,2,2,2,2,2,2] 
a = [2,8,22,1,4,22]
hash_set = set()

# This also works taking hash_set as empty list and appending items. But it is slower than adding to set.


def duplicate(arr):
   for j in arr:
      if j in hash_set:
         return True
      hash_set.add(j)
   return False
      

print(duplicate(a))
print(len(a))
print(len(hash_set))

