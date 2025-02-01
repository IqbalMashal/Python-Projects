class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1  # Fixed typo

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1  # Fixed typo
        return True

    def pop(self):
        if self.top is None:
            return None  # Changed return value for empty stack
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1  # Fixed typo
        return temp.value  # Return the popped value instead of True

    def print_stack(self):  # Added a method to display stack contents
        temp = self.top
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
stack = Stack(10)
stack.push(20)
stack.push(30)
stack.print_stack()  # Expected output: 30 -> 20 -> 10 -> None

print("Popped:", stack.pop())  # Expected output: Popped: 30
stack.print_stack()  # Expected output: 20 -> 10 -> None
