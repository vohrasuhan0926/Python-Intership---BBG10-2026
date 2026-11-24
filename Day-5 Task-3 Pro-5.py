class Stack:
    def __init__(self):
        self.__items = []  # Private list

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) > 0:
            return self.__items.pop()
        else:
            print("Stack is empty!")

    def __str__(self):
        return f"Stack: {self.__items}"


# Creating a stack object
s = Stack()

# Adding items
s.push(10)
s.push(20)
s.push(30)
s.push(40)

# Printing stack
print(s)

# Removing an item
print("Popped item:", s.pop())

# Printing stack after pop
print(s)