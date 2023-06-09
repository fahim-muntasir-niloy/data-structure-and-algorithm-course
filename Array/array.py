a_list = [1,2,3,4,5,6]
print(a_list)

from array import *

an_arr = array('i', [1,2,3,4,5])
another_arr = array('i', [1,2,35,4,5])

print(an_arr)
print(len(an_arr))


an_arr.append(-30)
print(an_arr)

str_arr = array('u', ['a','e','i','o','u'])
# str_arr = array('u', ['python','is','fun'])

print(str_arr)

import numpy as np

nparr = np.array([1,3,4,'abc'])
print((nparr))