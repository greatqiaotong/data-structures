"""
Implement the following functions to implement two stacks using a single array such that for storing elements
both stacks should use the same array. Initialize a Python list with the provided fixed size and perform all
the operations in-place without growing or shrinking the list!

push1(value)
- Input: an integer
- Output: inserts the given value in the first stack, i.e., stack1

push2(value)
- Input: an integer
- Output: inserts the given value in the second stack i.e stack2

pop1()
- Output: returns and removes the top value of stack1

pop2()
- Output: returns and removes the top value of stack2
"""

import sys


class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, value):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            print("Stack overflow")
            sys.exit(1)

    def push2(self, value):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print("Stack overflow")
            sys.exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack underflow")
            sys.exit(1)

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("Stack underflow")
            sys.exit(1)
