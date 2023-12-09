from src.LinkedList import LinkedList


def test_delete_by_value(odd_number_list):
    lst = odd_number_list
    lst.delete(10)

    expected1 = LinkedList()
    for i in range(10):
        expected1.insert_at_head(i)
    assert lst.are_identical(expected1)

    lst.delete(0)
    expected2 = LinkedList()
    for i in range(1, 10):
        expected2.insert_at_head(i)


def test_length(list_with_one_zero, list_with_two_zeroes):
    assert list_with_one_zero.length() == 1
    assert list_with_two_zeroes.length() == 2


def test_length_of_empty_list(empty_list):
    lst = empty_list
    assert lst.length() == 0
