#!/usr/bin/python3

"""
Singly linked list class

Class Node takes in integer values as data within each node,
and a next attribute which points to the next node or None

Class SinglyLinkedList initializes a default head to None
Method sorted_insert handles all nodes created and
adds them to the linked list sorted by the int value stored
"""


class Node:

    """Class that creates a single
    Node in a Singly Linked List
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):

        if not (value is None or type(value) is Node):
            raise TypeError("next must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    """Class that creates a
       Singly Linked List
    """

    def __init__(self):
        self.__head = None

    def __repr__(self):

        temp = self.__head
        count = ""
        while temp:
            count += "{:d}".format(temp.data)
            temp = temp.next_node
            if temp:
                count += "\n"
        return count

    def sorted_insert(self, value):

        if self.__head is None:
            self.__head = Node(value)
        else:
            current = self.__head
            previous = None
            while current and value > current.data:
                previous = current
                current = current.next_node
            if current is None:
                previous.next_node = Node(value)
            elif current is self.__head and previous is None:
                self.__head = Node(value, current)
            else:
                new = Node(value, current)
                previous.next_node = new
