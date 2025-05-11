# Node class represents a single element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # It stores Value of the node
        self.next = None  # Pointer to the next node in the list

# LinkedList class manages the list operations
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head (start) of the list

    # Insert a new node with given data at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        # If list is empty, new node becomes the head
        if not self.head:
            self.head = new_node
            return
        # Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next
        # Add the new node at the end
        temp.next = new_node

    # Insert a new node at the start of the list
    def insert_at_start(self, data):
        new_node = Node(data)
        # New node points to current head
        new_node.next = self.head
        # Update head to the new node
        self.head = new_node

    # Insert a new node at a specific index
    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Index must be non-negative")
        # If inserting at start, use insert_at_start
        if index == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        temp = self.head
        # Traverse to the node before the desired index
        for _ in range(index - 1):
            if not temp:
                raise IndexError("Index out of bounds")
            temp = temp.next
        if not temp:
            raise IndexError("Index out of bounds")
        # Insert new node at index
        new_node.next = temp.next
        temp.next = new_node

    # Delete a node at a specific index
    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        if not self.head:
            raise IndexError("List is empty")
        # If deleting the head node
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        # Traverse to the node before the one to delete
        for _ in range(index - 1):
            if not temp.next:
                raise IndexError("Index out of bounds")
            temp = temp.next
        # Remove the node by skipping it
        if not temp.next:
            raise IndexError("Index out of bounds")
        temp.next = temp.next.next

    # Search for a value in the list and return its index
    def search(self, value):
        temp = self.head
        index = 0
        # Traverse through the list to find the value
        while temp:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
        return -1  # Not found

    # Display all node values in the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
if __name__ == "__main__":
        ll = LinkedList()
        ll.insert_at_end(10)
        ll.insert_at_start(5)
        ll.insert_at_index(1, 7)
        ll.display()  
        print(ll.search(7)) 
        ll.delete_at_index(1)
        ll.display()
