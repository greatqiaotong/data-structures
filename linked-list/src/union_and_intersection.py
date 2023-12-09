from src.LinkedList import LinkedList
from src.remove_duplicates import remove_duplicates_brute_force as remove_duplicates


def union(lst_1: LinkedList, lst_2: LinkedList) -> LinkedList:
    if lst_1.is_empty():
        return lst_2

    curr = lst_1.get_head()
    while curr.next_element:
        curr = curr.next_element
    curr.next_element = lst_2.get_head()
    remove_duplicates(lst_1)
    return lst_1


def intersection(lst_1: LinkedList, lst_2: LinkedList) -> LinkedList:
    result = LinkedList()
    curr = lst_1.get_head()

    while curr:
        value = curr.data
        if lst_2.search(value):
            result.insert_at_head(value)
        curr = curr.next_element
    remove_duplicates(result)
    return result
