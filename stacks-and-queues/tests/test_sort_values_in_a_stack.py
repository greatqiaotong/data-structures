import pytest

from src.sort_values_in_a_stack import sort_stack_recursive, sort_stack_with_temp_stack
from src.Stack import MyStack


@pytest.fixture
def empty_stack():
    stack = MyStack()
    return stack


@pytest.fixture
def normal_stack():
    stack = MyStack()
    stack.push(23)
    stack.push(60)
    stack.push(12)
    stack.push(42)
    stack.push(4)
    stack.push(97)
    stack.push(2)
    return stack


def test_sort_empty_stack(empty_stack):
    assert sort_stack_with_temp_stack(empty_stack).is_empty()
    sort_stack_recursive(empty_stack)
    assert empty_stack.is_empty()


def test_sort_normal_stack_with_temp_stack(normal_stack):
    stack = normal_stack
    sorted_stack = sort_stack_with_temp_stack(stack)
    assert sorted_stack.stack_list == [97, 60, 42, 23, 12, 4, 2]


def test_sort_normal_stack_recursive(normal_stack):
    stack = normal_stack
    sort_stack_recursive(stack)
    assert stack.stack_list == [97, 60, 42, 23, 12, 4, 2]
