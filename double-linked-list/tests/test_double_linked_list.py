import pytest

from src.LinkedList import LinkedList


@pytest.fixture
def simple_list():
    lst = LinkedList()
    for i in range(11):
        lst.insert_at_head(i)
    return lst


@pytest.fixture
def list_with_one_node():
    lst = LinkedList()
    lst.insert_at_head(0)
    return lst


@pytest.fixture
def empty_list():
    lst = LinkedList()
    return lst


def test_delete_value_in_double_linked_list(simple_list):
    lst = simple_list
    lst.delete(10)

    expected1 = LinkedList()
    for i in range(10):
        expected1.insert_at_head(i)
    assert lst.are_identical(expected1)

    lst.delete(0)
    expected2 = LinkedList()
    for i in range(1, 10):
        expected2.insert_at_head(i)
    assert lst.are_identical(expected2)


def test_delete_value_one_node(list_with_one_node):
    lst = list_with_one_node
    lst.delete(0)

    assert lst.head_node == None


def test_delete_value_in_empty_list(empty_list):
    lst = empty_list
    assert lst.delete(0) == False
    assert lst.head_node == None
