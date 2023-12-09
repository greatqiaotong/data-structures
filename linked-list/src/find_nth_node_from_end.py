from typing import Any

from src.LinkedList import LinkedList


# Double iteration
def find_nth_double_iteration(lst: LinkedList, n: int) -> Any:
    length = lst.length()
    if length == 0:
        raise Exception("List is empty!")
    if n > length or n <= 0:
        raise ValueError("n should be smaller than list length and larger than 0.")

    position = 0
    curr = lst.get_head()
    while curr:
        if position == length - n:
            return curr.data
        curr = curr.next_element
        position += 1


# Two pointers - time complexity O(n)
def find_nth_two_pointers(lst: LinkedList, n: int) -> Any:
    # 1. Move end_node forward n times, while nth_node stays at the head
    # 2. If end_node becomes None, n was out of bounds of the array. Return -1 to indicate that the node is not found.
    # 3. Once end_node is at nth position from the start, move both end_node and nth_node pointers simultaneously.
    # 4. When end_node reaches the end, nth_node is at the Nth position from the end
    # 5. Return the node’s value

    length = lst.length()
    if length == 0:
        raise Exception("List is empty!")
    if n > length or n <= 0:
        raise ValueError("n should be smaller than list length and larger than 0.")

    nth_node = lst.get_head()
    end_node = lst.get_head()

    count = 0
    while count < n:
        end_node = end_node.next_element
        count += 1

    while end_node:
        end_node = end_node.next_element
        nth_node = nth_node.next_element
    return nth_node.data
