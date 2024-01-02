"""
Implement a function called sort_stack() which takes a stack and sorts all of its elements in
ascending order such that when they are popped and printed, they come out in ascending order.
So the element that was pushed last to the stack has to be the smallest.

- Input: A stack of integers.
- Output: The stack with all its elements sorted in descending order.
"""
from src.Stack import MyStack
from typing import Any


def sort_stack_with_temp_stack(stack: MyStack) -> MyStack:
    temp_stack = MyStack()
    while not stack.is_empty():
        value = stack.pop()
        if temp_stack.peek() is not None and value >= temp_stack.peek():
            temp_stack.push(value)
        else:
            while not temp_stack.is_empty() and value < temp_stack.peek():
                stack.push(temp_stack.pop())
            temp_stack.push(value)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return stack


def sort_stack_recursive(stack: MyStack) -> MyStack:
    if not stack.is_empty():
        value = stack.pop()
        sort_stack_recursive(stack)
        insert(stack, value)


def insert(stack: MyStack, value: Any) -> MyStack:
    if stack.is_empty() or value < stack.peek():
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)
