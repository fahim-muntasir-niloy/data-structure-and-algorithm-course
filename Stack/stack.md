# Stack in Python

Stack is a data structure similar to list. This is called stack due to its `LIFO` or `Last In First Out` structure.

There are some basic operations that allow us to perform different actions on a stack.

- Push: Add an element to the top of a stack
- Pop: Remove an element from the top of a stack
- IsEmpty: Check if the stack is empty
- IsFull: Check if the stack is full
- Peek: Get the value of the top element without removing it

> Stack-based problems are considered as so easy, but Monotonic Stacks are generally used to solve medium to hard-level problems.

## Monotonic Stack
Monotonic stacks can be used to solve many problems in linear time that would otherwise require quadratic time complexity. Some examples of problems that can be solved using a monotonic stack include finding the nearest smaller element on the left or right side of an array element, finding the maximum area of a histogram, and solving the sliding window maximum problem.

`Monotonic` = It is a word for mathematics functions. A function $y = f(x)$ is monotonically increasing or decreasing when it follows the below conditions: 

- As x increases, y also increases always, then it’s a monotonically increasing function.
- As x increases, y decreases always, then it’s a monotonically decreasing function.

$y = 2x +5,$ it’s a monotonically increasing function.\
$y = -(2x)$, it’s a monotonically decreasing function.  