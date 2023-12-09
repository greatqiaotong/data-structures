from __future__ import annotations

from src.Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self) -> Node:
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_head(self, value):
        temp_node = Node(value)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node

        temp_node.next_element = self.head_node
        self.head_node.previous_element = temp_node
        self.head_node = temp_node
        return self.head_node

    def delete(self, value):
        deleted = False
        if self.is_empty():
            return deleted

        current_node = self.head_node
        if current_node.data == value:
            self.head_node = current_node.next_element
            if current_node.next_element:
                current_node.next_element.previous_element = None
                deleted = True
            return deleted

        while current_node:
            if current_node.data == value:
                if current_node.next_element:
                    prev_node = current_node.previous_element
                    next_node = current_node.next_element
                    prev_node.next_element = next_node
                    next_node.previous_element = prev_node
                else:
                    current_node.previous_element.next_element = None
                deleted = True
                break
            current_node = current_node.next_element
        return deleted

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
