# Big O Notation
This is a representation of complexity of the code. This is also dependent upon the input. In `Big O`, there are six major types of complexities (time and space):

- Constant: O(1) --- Best
- Linear time: O(n) --- Fair
- Logarithmic time: O(n log n) --- Good
- Quadratic time: O(n^2) --- Bad
- Exponential time: O(2^n) --- Bad
- Factorial time: O(n!) --- Horrible


# Time complexity
Time required for a code to compile or produce output based on the input. It doesnt necessarily mean that the algorithm used, will be the fastest all the time in every scenario.

1. When your calculation is not dependent on the input size, it is a constant time complexity $(O(1))$.

2. When the input size is reduced by half, maybe when iterating, handling recursion, or whatsoever, it is a logarithmic time complexity $(O(log n))$.

3. When you have a single loop within your algorithm, it is linear time complexity $(O(n))$.

4. When you have nested loops within your algorithm, meaning a loop in a loop, it is quadratic time complexity $(O(n^2))$.

5. When the growth rate doubles with each addition to the input, it is exponential time complexity $(O(2^n))$.


# Space Complexity
Memory or, storage space required for a code to compile, including the space of input values for execution. The best algorithm/program should have a low level of space complexity. The less space required, the faster it executes.



## Reference
1. [Theoretical approach of Time and space complexity](https://www.simplilearn.com/tutorials/data-structure-tutorial/time-and-space-complexity#:~:text=Time%20complexity%20is%20a%20function,of%20input%20to%20the%20method.)

2. [Big O Cheat Sheet – Time Complexity Chart](https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/)