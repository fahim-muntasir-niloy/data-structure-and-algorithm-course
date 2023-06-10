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

```py
my_set.add("GO")
print(my_set)

# output
# {'GO'}
```


```python
my_set.update(["python","Java","C++"])
print(my_set)

# output
# {'Java', 'C++', 'python'}
```

```python
my_set.remove("Java")
print(my_set)

# output
# {'GO', 'Python', 'C++'}
```

So, we can see the outputs are coming in a random order. Now, lets see what happens if we add duplicate items.

```py
my_set.add("C++")
print(my_set)

# output
# {'C++', 'Java', 'GO', 'Python'}
```
C++ wasn't added again, as it had already that item. `Sets` are very much useful in finding unique items in an array, it also removes duplicates, which you will see in the code.

## References
1. [Sets in Python](https://www.w3schools.com/python/python_sets.asp)