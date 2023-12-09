import pytest

from src.find_nth_node_from_end import find_nth_double_iteration, find_nth_two_pointers


def test_find_nth_empty_list(empty_list):
    with pytest.raises(Exception, match="List is empty!"):
        find_nth_double_iteration(empty_list, 5)


def test_find_nth_invalid_n(even_number_list):
    with pytest.raises(
        ValueError, match="n should be smaller than list length and larger than 0."
    ):
        find_nth_double_iteration(even_number_list, 0)

    with pytest.raises(
        ValueError, match="n should be smaller than list length and larger than 0."
    ):
        find_nth_double_iteration(even_number_list, -1)

    with pytest.raises(
        ValueError, match="n should be smaller than list length and larger than 0."
    ):
        find_nth_double_iteration(even_number_list, 11)


def test_find_nth(even_number_list):
    assert find_nth_double_iteration(even_number_list, 1) == 0
    assert find_nth_double_iteration(even_number_list, 2) == 1


def test_find_nth_empty_list(empty_list):
    with pytest.raises(Exception, match="List is empty!"):
        find_nth_two_pointers(empty_list, 5)


def test_find_nth_invalid_n(even_number_list):
    with pytest.raises(
        ValueError, match="n should be smaller than list length and larger than 0."
    ):
        find_nth_two_pointers(even_number_list, 0)

    with pytest.raises(
        ValueError, match="n should be smaller than list length and larger than 0."
    ):
        find_nth_two_pointers(even_number_list, -1)

    with pytest.raises(
        ValueError, match="n should be smaller than list length and larger than 0."
    ):
        find_nth_two_pointers(even_number_list, 11)


def test_find_nth(even_number_list):
    assert find_nth_two_pointers(even_number_list, 1) == 0
    assert find_nth_two_pointers(even_number_list, 2) == 1
