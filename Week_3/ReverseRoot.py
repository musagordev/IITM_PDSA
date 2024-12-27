# Function reverse(root) that will reverse the linked list with the first node passed as an argument, and return the first node of the reversed list. Each node in the linked list is an object of class Node. 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def isEmpty(self):
        return self.next is None


def reverse(root):
    prev = None
    current = root

    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the pointer
        prev = current  # Move prev and current one step forward
        current = next_node

    return prev
