# Array in Python
An array and a list seems to be similar at first glance, but they aren't. A list can be formed with any types of items, let it be integer or float or string. These items can co exist in a list.

```python
a_list = [1,2,3,'abc', 'python', 0]
```

On the other hand, an array is very much strict with declaration of the data type of the items. However, an array will support all the methods found with a list.

```py
from array import *

an_array = array('i', [1,2,3,4,5,6])

another_arr = array('i', [1,2,3.5,4,5])  # for float use 'f'

# _______ Output _________
# another_arr = array('i', [1,2,3.5,4,5])
# TypeError: 'float' object cannot be interpreted as an integer
```
Here, an array constructor is called at first. The constructor has two parts.

```py
array('typecode', [array elements])
```
`Typecode` means the data type of the array elements. As said before, an array will only accept fixed data type items. Unfortunately, an array doesn't take strings more than one character.

```py
str_arr = array('u',['a','e','i','o','u'])  # accepted

# Ouput
# array('u', 'aeiou')

str_arr = array('u', ['python','is','fun']) # error

# Output
# str_arr = array('u', ['python','is','fun'])
# TypeError: array item must be unicode character
```

#### Can you spot something interesting at the outputs?

To solve this issue, `numpy` library cam with it's own `numpy.ndarray` class items. 

```py
import numpy as np

np_arr = np.array([1,3,4,'abc'])
print(type(np_arr))
print(nparr)

# Output
<class 'numpy.ndarray'>
['1' '3' '4' 'abc']
```
However, this converts all the items into strings as we can see.

## Array vs Lists
Lists and arrays both are mutable and store ordered items. List can store elements of different types, but arrays can store elements only of the same type. List provides more flexibility as it doesn't require explicit looping, but arrays require explicit looping to print elements.

## References
1. [Array and its methods](https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods/)