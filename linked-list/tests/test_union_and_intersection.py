from src.LinkedList import LinkedList
from src.union_and_intersection import intersection, union


def test_union_two_empty_list(empty_list):
    new_list = union(empty_list, empty_list)
    assert new_list.is_empty()


def test_union_first_list_empty(empty_list, list_with_one_zero):
    new_list = union(empty_list, list_with_one_zero)
    assert new_list.are_identical(list_with_one_zero)


def test_union_second_list_empty(empty_list, list_with_one_zero):
    new_list = union(list_with_one_zero, empty_list)
    assert new_list.are_identical(list_with_one_zero)


def test_union():
    list_1 = LinkedList()
    list_1.insert_at_head(8)
    list_1.insert_at_head(22)
    list_1.insert_at_head(15)

    list_2 = LinkedList()
    list_2.insert_at_head(21)
    list_2.insert_at_head(14)
    list_2.insert_at_head(7)

    expected = LinkedList()
    expected.insert_at_head(8)
    expected.insert_at_head(22)
    expected.insert_at_head(15)
    expected.insert_at_head(21)
    expected.insert_at_head(14)
    expected.insert_at_head(7)

    new_list = union(list_1, list_2)
    new_list.are_identical(expected)


def test_intersection_two_empty_list(empty_list):
    new_list = intersection(empty_list, empty_list)
    assert new_list.is_empty()


def test_intersection_first_list_empty(empty_list, list_with_one_zero):
    new_list = intersection(empty_list, list_with_one_zero)
    assert new_list.is_empty()


def test_intersection_second_list_empty(empty_list, list_with_one_zero):
    new_list = intersection(empty_list, list_with_one_zero)
    assert new_list.is_empty()


def test_intersection():
    list_1 = LinkedList()
    list_1.insert_at_head(14)
    list_1.insert_at_head(22)
    list_1.insert_at_head(15)

    list_2 = LinkedList()
    list_2.insert_at_head(21)
    list_2.insert_at_head(14)
    list_2.insert_at_head(15)

    expected = LinkedList()
    expected.insert_at_head(14)
    expected.insert_at_head(15)

    new_list = intersection(list_1, list_2)
    new_list.are_identical(expected)
