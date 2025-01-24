class Stack_Advance:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if self.stack is None:
            self.stack += [item]
        else:
            self.stack+= [item]
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def pop(self):
        if not self.is_empty():
            temp_stack = self.stack[:-1]
            self.stack = temp_stack
        else:
            print("Stack is not empty")

    def size(self):
        print("Size of the Stack:-", len(self.stack))
        
    def peek(self):
        if not self.is_empty():
            print("Stack Top element:-", self.stack[-1])
        
    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i], end=" ")
        print()


# Example Usage
stack = Stack_Advance()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print("Initial Stack: ", end="")
stack.display()
print("\nStack Size: ", end="")
stack.size()

stack.push(60)
print("Stack after insertion: ", end="")
stack.display()
print("Delete Element from Stack:-")
stack.pop()
stack.display()
stack.size()
stack.peek()