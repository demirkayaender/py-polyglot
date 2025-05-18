# Iterating over a list
print("Iterating over a list")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Iterating over a list with index
print("Iterating over a list with index")
for i, num in enumerate(numbers):
    print(f"Index {i}: {num}")

# Iterating over a range
print("Iterating over a range")
for i in range(5):
    print(i)

# Iterating with foreach
print("Iterating with foreach")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"Current fruit: {fruit}")

# Iterating over a dictionary
print("Iterating over a dictionary")
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(f"Key: {key}, Value: {person[key]}")

# Iterating over dictionary items
print("Iterating over dictionary items")
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

# While loop
print("While loop")
count = 0
while count < 5:
    print(count)
    count += 1

# List comprehension
print("List comprehension")
squares = [x*x for x in range(5)]
print(squares)

# Dictionary comprehension
print("Dictionary comprehension")
square_dict = {x: x*x for x in range(5)}
print(square_dict)

# Iterating through a linked list
print("Iterating through a linked list")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Create and populate linked list
linked_list = LinkedList()
for i in range(1, 6):
    linked_list.append(i)

# Iterate through linked list
print("Iterating through linked list:")
current = linked_list.head
while current:
    print(current.data)
    current = current.next
