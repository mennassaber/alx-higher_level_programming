#!/usr/bin/python3
"""Define classes for a singly linked list."""


class Node:
    """Represent a node in a singly linked list."""
    
    def __init__(self, data, next_node=None):
        """Initialize a new node.
        
        Args:
            data: The data to store in the node.
            next_node (Node): The next node in the list (default None).
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """Get or set the data stored in the node."""
        return self.__data
    
    @data.setter
    def data(self, value):
        """Set the data stored in the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """Get or set the next node."""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """Set the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list."""
    
    def __init__(self):
        """Initialize a new singly linked list."""
        self.head = None
    
    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position in the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    
    def __str__(self):
        """Return a string representation of the list."""
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
