"""
Example:
exp = "921 * - 8 - 4 +" # 9 - 2 * 1 - 8 + 4
output = 3
"""
from src.Stack import MyStack


def eval_post_fix(exp: str) -> int:
    stack = MyStack()
    try:
        for char in exp:
            if char.isdigit():
                stack.push(char)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))
        return int(stack.pop())
    except TypeError:
        return "Invalid sequence"
