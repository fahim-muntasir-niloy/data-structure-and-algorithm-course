# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

arr_1 = [2,4,3]
arr_2 = [5,6,4]

# arr.reverse()

# str_arr = "".join(map(str,arr))

def addList(l1,l2):
    l1.reverse()
    l2.reverse()
    
    l1_str = "".join(map(str, l1))
    l2_str = "".join(map(str, l2))
    
    print(int(l1_str)+int(l2_str))

addList(arr_1, arr_2)
