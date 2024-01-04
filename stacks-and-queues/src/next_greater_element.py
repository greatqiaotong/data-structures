"""
For each element i in a list, the function finds the first element to its right
which is greater than element i. If for any element such a value does not exist,
the answer is -1.

- Input: an integer list.
- Output: a list containing the next greater element of each element from the
input list.

- Sammple input: list = [4, 6, 3, 2, 8, 1]
- Sample output: result = [6, 8, 8, 8, -1, -1]
"""
from src.Stack import MyStack


def next_greater_element(lst: list[int]) -> list[int]:
    stack = MyStack()

    result = [-1] * len(lst)
    for i in range(len(lst) - 1, -1, -1):
        while not stack.is_empty() and lst[i] >= stack.peek():
            stack.pop()
        if not stack.is_empty():
            result[i] = stack.peek()
        stack.push(lst[i])

    return result
