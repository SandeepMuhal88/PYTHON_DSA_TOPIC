# Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        print("None", end="<-->")
        current = self.head
        while current:
            print(f"{current.data}<-->", end="")
            current = current.next
        print("None")
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def insert_at_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    
    def inset_by_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        current = self.head
        prev = None
        count = 0
        while current:
            if count == index:
                prev.next = new_node
                new_node.prev = prev
                new_node.next = current
                current.prev = new_node
                return
            prev = current
            current = current.next
            count += 1
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
    
    def delete_at_first(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next
        self.head.prev = None
    
    def delete_at_last(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None
        current.prev = None
        print("None", end="<-->")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")
    
    def delete_by_index(self, index):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        prev = None
        count = 0
        while current:
            if count == index:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            count += 1
        print("Index not found")
    
    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            current.prev = next
            prev = current
            current = next
        self.head = prev
        print("None", end="<-->")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")
    


dll = DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.insert(40)
dll.insert(50)
dll.insert(60)
dll.insert(70)
dll.insert(80)
dll.insert(90)
dll.insert(100)
dll.display()
dll.delete(20)
dll.display()
dll.delete_at_first()
dll.display()
dll.delete_at_last()
dll.display()
dll.delete_by_index(3)
dll.display()
dll.reverse()
dll.display()