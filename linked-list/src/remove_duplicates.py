from src.LinkedList import LinkedList


def remove_duplicates_brute_force(lst: LinkedList) -> LinkedList:
    if lst.is_empty():
        return None

    curr = lst.get_head()
    if curr.next_element is None:
        return lst

    unique: list = []
    unique.append(curr.data)
    while curr.next_element:
        if curr.next_element.data not in unique:
            unique.append(curr.next_element.data)
            curr = curr.next_element
        else:
            curr.next_element = curr.next_element.next_element
    return lst


def remove_duplicates_inner_outer_iteration(lst: LinkedList) -> LinkedList:
    if lst.is_empty():
        return None

    curr = lst.get_head()
    if curr.next_element is None:
        return lst

    outer = curr
    while outer:
        inner = outer
        while inner:
            if inner.next_element:
                if outer.data == inner.next_element.data:
                    inner.next_element = inner.next_element.next_element
                else:
                    inner = inner.next_element
            else:
                inner = inner.next_element
        outer = outer.next_element
    return lst
