class Stack:
    def __init__(self):
        self.stack = []  # Using a list to store stack elements

    def push(self, value):
        self.stack.append(value)  # Append adds to the top of the stack

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()  # Pop removes from the top of the stack

    def peek(self):  
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]  # Peek at the top element without removing

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
