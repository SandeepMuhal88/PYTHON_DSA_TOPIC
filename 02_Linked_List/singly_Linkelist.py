class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")
    
    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def update(self, index, data):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        while current:
            if current.data == index:
                current.data = data
                return
            current = current.next
        print("Index not found")

    def delete(self, index):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        prev = None
        while current:
            if current.data == index:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        print("Index not found")

    def inset_by_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        prev = None
        count = 0
        while current:
            if count == index:
                prev.next = new_node
                new_node.next = current
                return
            prev = current
            current = current.next
            count += 1


