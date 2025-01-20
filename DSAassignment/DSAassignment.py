
class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

class Stack:
    def _init_(self):
        self.top = None

    def add(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Added {value} to the stack.")

    def remove(self):
        if self.is_empty():
            return "Stack is empty!"
        removed = self.top.value
        self.top = self.top.next
        return f"Removed: {removed}"

    def peek_top(self):
        if self.is_empty():
            return "Stack is empty!"
        return f"Top value: {self.top.value}"

    def is_empty(self):
        return self.top is None

    def show(self):
        current = self.top
        print("Stack elements:")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

class Queue:
    def _init_(self):
        self.front = self.rear = None

    def add(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Added {value} to the queue.")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Added {value} to the queue.")

    def remove(self):
        if self.is_empty():
            return "Queue is empty!"
        removed = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return f"Removed: {removed}"

    def peek_front(self):
        if self.is_empty():
            return "Queue is empty!"
        return f"Front value: {self.front.value}"

    def is_empty(self):
        return self.front is None

    def show(self):
        current = self.front
        print("Queue elements:")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Stack and Queue operations
if _name_ == "_main_":
    # Stack operations
    print("Stack Operations:")
    stack = Stack()
    stack.add(5)
    stack.add(10)
    stack.add(15)
    stack.show()
    print(stack.remove())
    print(stack.peek_top())
    stack.show()
    print()

    # Queue operations
    print("Queue Operations:")
    queue = Queue()
    queue.add(3)
    queue.add(2)
    queue.add(1)
    queue.show()
    print(queue.remove())
    print(queue.peek_front())
    queue.show()