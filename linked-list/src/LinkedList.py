from __future__ import annotations

from src.Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self, value):
        temp_node = Node(value)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return

    def insert_at_tail(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head_node = new_node
            return

        temp = self.head_node
        while temp.next_element:
            temp = temp.next_element

        temp.next_element = new_node
        return

    def search(self, value):
        if self.is_empty():
            return False

        temp = self.head_node
        while temp:
            if temp.data == value:
                return True
            temp = temp.next_element
        return False

    def delete_at_head(self):
        first_element = self.head_node

        if first_element:
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def delete(self, value):
        deleted = False
        if self.is_empty():
            return deleted

        previous_node = Node(None)
        current_node = self.head_node
        if current_node.data == value:
            deleted = True
            self.delete_at_head()
            return deleted

        while current_node:
            if current_node.data == value:
                deleted = True
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                break
            previous_node = current_node
            current_node = current_node.next_element
        return deleted

    def length(self):
        current_node = self.head_node
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next_element
        return count

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False

        temp = self.head_node
        while temp.next_element:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def are_identical(self, lst_b: LinkedList):
        a = self.get_head()
        b = lst_b.get_head()
        while a != None and b != None:
            if a.data != b.data:
                return False
            a = a.next_element
            b = b.next_element
        return a == None and b == None
