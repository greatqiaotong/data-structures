import pytest

from src.Queue import MyQueue
from src.reverse_first_k_elements_in_a_queue import reverseK


@pytest.fixture
def empty_queue():
    queue = MyQueue()
    return queue


@pytest.fixture()
def normal_queue():
    queue = MyQueue()
    for i in range(10):
        queue.enqueue(i + 1)
    return queue


def test_reverseK_negative_k(normal_queue):
    queue = normal_queue
    assert reverseK(queue, -1) == None


def test_reverseK_invalid_k(normal_queue):
    queue = normal_queue
    assert reverseK(queue, 11) == None


def test_reverseK_empty_queue(empty_queue):
    queue = empty_queue
    assert reverseK(queue, 10) == None


def test_reverseK(normal_queue, capfd):
    queue = normal_queue
    result = reverseK(queue, 5)
    result.print_list()
    out, err = capfd.readouterr()
    assert out == "[5, 4, 3, 2, 1, 6, 7, 8, 9, 10]\n"
