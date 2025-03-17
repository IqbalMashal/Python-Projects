class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:   
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1  # Initialize length correctly

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value, end=" -> " if temp.next else "")
            temp = temp.next
        print()  # Add newline for better formatting

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:  # Queue is empty
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1  # Increment length

    def dequeue(self):
        if self.length == 0:  # Queue is empty
            return None
        temp = self.first
        if self.first == self.last:  # Only one element in queue
            self.last = None
            self.first = None
        else:
            self.first = self.first.next
            temp.next = None  # Remove reference to next node
        self.length -= 1  # Decrement length
        return temp.value  # Return dequeued value
