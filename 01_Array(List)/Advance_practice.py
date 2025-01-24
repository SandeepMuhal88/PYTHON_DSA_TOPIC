class Array:
    def __init__(self):
        self.array = []

    def insert_element(self, value, index=None):
        if index is None:
            self.array += [value]
        else:
            if index < 0 or index > len(self.array):
                print("Invalid index")
                return
            new_array = []
            # for i in range(len(self.array) + 1):
            #     if i < index:
            #         new_array += [self.array[i]]
            #     elif i == index:
            #         new_array += [value]
            #     else:
            #         new_array += [self.array[i - 1]]
            # self.array = new_array
            self.array = self.array[:index] + [value] + self.array[index:]

    def delete_element(self, index):

        if index < 0 and index >= len(self.array):
            print("Invalid index")
            return
        new_array = []
        # for i in range(len(self.array)):
        #     if i != index:
        #         new_array += [self.array[i]]
        # self.array = new_array
        self.array = self.array[:index] + self.array[index + 1:]

    def display(self):

        for i in range(len(self.array)):
            print(self.array[i], end=" ")
        print()

    def size(self):
        print(len(self.array))
# Example Usage
arr = Array()
arr.insert_element(10,0)
arr.insert_element(20,1)
arr.insert_element(30,2)
arr.insert_element(40,3)
arr.insert_element(50,4)
print("Initial Array: ", end="")
arr.display()

arr.insert_element(60, 5)
print("Array after insertion: ", end="")
arr.display()
arr.size()
arr.delete_element(2)
arr.display()
# print("Array after deletion: ", end="")
# arr.display()
