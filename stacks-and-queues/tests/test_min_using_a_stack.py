from src.min_using_a_stack import MinStack


def test_min_using_a_stack():
    stack = MinStack()
    stack.push(5)
    stack.push(0)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(0)
    assert stack.min() == 0

    stack.pop()
    stack.push(-2)
    assert stack.min() == -2

    stack.pop()
    assert stack.min() == 0
