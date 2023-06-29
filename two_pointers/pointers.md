# Pointers in Python

A pointer is a variable that stores the address of another variable. Unlike other variables that hold values of a certain type, pointer holds the address of a variable.

> For example, an integer variable holds (or you can say stores) an integer value, however an integer pointer holds the address of a integer variable.

Pointers are memory locations, that can refer to an exact location in the computer memory. Using pointers goes against the purpose of being simple of python.

> Python natively doesn't support pointers like C/ C++. In python, pointers are mainly used to move between items of an array.

For example:

```py
stringPiece = "A_big_Sentance"

pointer = len(stringPiece)-1  # 14-1 = 13

while pointer>=0:
    print(f"{pointer} ------- {stringPiece[pointer]}")
    pointer-=1

""" Output
13 ------- e
12 ------- c
11 ------- n
10 ------- a
9 ------- t
8 ------- n
7 ------- e
6 ------- S
5 ------- _
4 ------- g
3 ------- i
2 ------- b
1 ------- _
0 ------- A
"""
```

This type of implicit pointing can be used in many cases, such as reversing an array, finding duplicates and many more.