from src.remove_duplicates import (
    remove_duplicates_brute_force,
    remove_duplicates_inner_outer_iteration,
)


def test_remove_duplicates_brute_force(
    empty_list, list_with_one_zero, list_with_two_zeroes
):
    remove_duplicates_brute_force(empty_list)
    assert empty_list.is_empty()
    assert remove_duplicates_brute_force(list_with_one_zero).are_identical(
        list_with_one_zero
    )
    assert remove_duplicates_brute_force(list_with_two_zeroes).are_identical(
        list_with_one_zero
    )


def test_remove_duplicates_inner_outer_iteration(
    empty_list, list_with_one_zero, list_with_two_zeroes
):
    remove_duplicates_inner_outer_iteration(empty_list)
    assert empty_list.is_empty()
    assert remove_duplicates_inner_outer_iteration(list_with_one_zero).are_identical(
        list_with_one_zero
    )
    assert remove_duplicates_inner_outer_iteration(list_with_two_zeroes).are_identical(
        list_with_one_zero
    )
