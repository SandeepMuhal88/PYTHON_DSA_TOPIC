#CREATE Simple array using List data structure
# An array is a data structure used to store a collection of elements, typically of the same type, in a contiguous block of memory.
#  While Python doesn't have a built-in array type like lower-level
#  languages (e.g., C++), the list in Python can serve as a dynamic array.

# We make an array using List but that have same type of elements
class Array:
    def __init__(self):
        self.array = []

    def add(self, item):
        self.array.append(item)

    def remove(self, item):
        self.array.remove(item)

    def get(self, index):
        return self.array[index]

    def size(self):
        return len(self.array)
    
    def display(self):
        print(self.array)


arr = Array()
num=int(input("Enter the size of array: "))
for i in range(num):
    arr.add(int(input(f"Enter the element for index {i}: ")))
    

print(arr.get(0))
print(arr.size())
arr.display()

arr.remove(1)
arr.display()