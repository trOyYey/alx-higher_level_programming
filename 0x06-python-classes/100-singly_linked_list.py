#!/usr/bin/python3
"""Square module."""


class Node:
    """defining named square"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns value of size"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets value of size"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """returns value of next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets tje next node value"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """as in singly linked lists"""
    __head = None

    def __init__(self):
        """initalizing"""
        pass

    def __str__(self):
        """as in print() in singly linked lists"""
        if self.__head is None:
            return ''
        temp = self.__head
        string = ''
        while temp.next_node is not None:
            string += str(temp.data) + '\n'
            temp = temp.next_node
        return string + str(temp.data)

    def sorted_insert(self, value):
        """inserts new node to singly linked lists"""
        if (self.__head is None or self.__head.data >= value):
            self.__head = Node(value, self.__head)
            return

        temp = self.__head
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node
        temp.next_node = Node(value, temp.next_node)
