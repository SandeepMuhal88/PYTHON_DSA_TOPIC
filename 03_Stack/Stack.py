# Q1 what is stack ?

# stack = first in last out or last in first out
#LIFO & FILO
#
#
# stack operation
# 1. append = data push kerna
# 2. pop = delete kerna (last item will deleted)
# 3. is empty
# 4. length
# 5. top element

# Q2. implement stack with function ?
stack=[]
def push(item):
    stack.append(item)

def is_empty():
    if len(stack) ==0:
        return True
    else:
        return False
# return len(stack)==0


def pop():
    if not is_empty():
        stack.pop()
        # IT is delete Value Always Last value
    else:
        print("Stack is empty:)))")
    

def size():
    print("Size of the Stack:-",len(stack))

def peek():
    if not is_empty:
        print("Sacks Top element:-",stack[-1])



push(104)
push(200)
push(303)
push(154)
push(111)
pop()
print(is_empty())
size()
peek()