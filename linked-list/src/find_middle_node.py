from typing import Any

from src.LinkedList import LinkedList


def find_mid_brute_force(lst: LinkedList) -> Any:
    if lst.is_empty():
        return None

    length = lst.length()
    if length % 2 == 1:
        mid = length // 2
    else:
        mid = length // 2 - 1

    curr = lst.get_head()
    position = 0

    while position < mid:
        curr = curr.next_element
        position += 1
    return curr.data


# Two pointers
def find_mid_two_pointers(lst: LinkedList) -> Any:
    if lst.is_empty():
        return None

    if lst.length() == 1:
        return lst.get_head().data

    curr = lst.get_head()
    mid = curr
    curr = curr.next_element.next_element
    while curr:
        mid = mid.next_element
        curr = curr.next_element
        if curr:
            curr = curr.next_element
    return mid.data
