import pytest

from src.LinkedList import LinkedList


@pytest.fixture(scope="session")
def empty_list():
    lst = LinkedList()
    return lst


@pytest.fixture(scope="session")
def list_with_one_zero():
    lst = LinkedList()
    lst.insert_at_head(0)
    return lst


@pytest.fixture(scope="session")
def list_with_two_zeroes():
    lst = LinkedList()
    lst.insert_at_head(0)
    lst.insert_at_head(0)
    return lst


@pytest.fixture(scope="session")
def even_number_list():
    lst = LinkedList()
    for i in range(10):
        lst.insert_at_head(i)
    return lst


@pytest.fixture(scope="session")
def odd_number_list():
    lst = LinkedList()
    for i in range(11):
        lst.insert_at_head(i)
    return lst
