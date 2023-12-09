import pytest

from src.find_middle_node import find_mid_brute_force, find_mid_two_pointers


@pytest.mark.parametrize(
    "lst, expected",
    [
        ("empty_list", None),
        ("list_with_one_zero", 0),
        ("even_number_list", 5),
        ("odd_number_list", 5),
    ],
)
def test_find_mid_brute_force(lst, expected, request):
    lst = request.getfixturevalue(lst)
    assert find_mid_brute_force(lst) == expected


@pytest.mark.parametrize(
    "lst, expected",
    [
        ("empty_list", None),
        ("list_with_one_zero", 0),
        ("even_number_list", 5),
        ("odd_number_list", 5),
    ],
)
def test_find_mid_two_pointers(lst, expected, request):
    lst = request.getfixturevalue(lst)
    assert find_mid_two_pointers(lst) == expected
