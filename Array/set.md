# Set in Python

Sets are lists with `curly braces`, that only stores unique values. These dont have any order. They have almost all the `list` methods.

```python
my_set = set()  # declaring blank set
print(type(my_set))

# Output
# <class 'set'>
```
## Items in Set
Once a set is declared, the items can be updated. New items can be added and items can be removed as well.

```python
my_set.update(["python","Java","C++"])
print(my_set)

# output
# {'Java', 'C++', 'python'}
```

