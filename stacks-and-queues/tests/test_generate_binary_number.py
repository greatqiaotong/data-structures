from src.generate_binary_numbers import find_bin


def test_find_bin():
    actual_1 = find_bin(3)
    expected_1 = ["1", "10", "11"]
    assert actual_1 == expected_1

    actual_2 = find_bin(4)
    expected_2 = ["1", "10", "11", "100"]
    assert actual_2 == expected_2
