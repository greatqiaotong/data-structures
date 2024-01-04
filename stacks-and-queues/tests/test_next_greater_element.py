from src.next_greater_element import next_greater_element


def test_next_greater_element():
    lst1 = [4, 6, 3, 2, 8, 1]
    expected1 = [6, 8, 8, 8, -1, -1]
    assert next_greater_element(lst1) == expected1

    lst2 = [4, 8, 14, 2, 16, 18, 9, 5]
    expected2 = [8, 14, 16, 16, 18, -1, -1, -1]
    assert next_greater_element(lst2) == expected2

    lst3 = [13, 3, 12, 16, 15, 11, 1, 2]
    expected3 = [16, 12, 16, -1, -1, -1, 2, -1]
    assert next_greater_element(lst3) == expected3
