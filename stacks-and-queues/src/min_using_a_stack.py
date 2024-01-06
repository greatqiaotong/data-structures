"""
Implement the MinStack class which will have a min() function. Whenever min()
is called, the minimum value of the stack is returned in O(1) time. The element
is not popped from the stack. Its value is simply returned.

- Input: min() operates on an object of MinStack and doesn’t take any input
- Output: Returns minimum number in O(1) time
"""
from src.Stack import MyStack


class MinStack:
    def __init__(self):
        self.min_stack = MyStack()
        self.main_stack = MyStack()

    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or value < self.min_stack.peek():
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())

    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()
        return None
