
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index): 
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev = self.get(index-1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return True
        
    def reverse(self):
        if self.head is None:  # Check if the list is empty
            return

        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None

        # Reverse the linked list
        for _ in range(self.length):  # Use a for loop to iterate through the list
            after = temp.next  # Store the next node
            temp.next = before  # Reverse the link
            before = temp  # Move before one step forward
            temp = after  # Move temp one step forward

        # After the loop, set the new head and tail
        self.tail.next = None  # Set the new tail's next to None

                # for _ in range(self.length): for loop method
                    # after = temp.next
                    # temp.next = before
                    # before = temp
                    # temp = after

        
    def find_middle_node(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        while fast.next and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def partition_list(self, value):
        if self.head is None:
            return None
            
        greater_dummy = Node(0)
        less_dummy = Node(0)
        
        less = less_dummy
        greater = greater_dummy
        
        current = self.head
        
        while current:
            if current.value < value:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        greater.next = None
        less.next = greater_dummy.next
        
        self.head = less_dummy.next
        self.tail = greater
        
        return self.head


def find_kth_from_end(linkedList, value):
    if value < 0:
        return None
        
    slow = linkedList.head
    fast = linkedList.head
    
    for _ in range(value):
        if fast is None:
            return None
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow


 
my_linked_list1 = LinkedList(4)
my_linked_list1.append(5)
my_linked_list1.prepend(6)

my_linked_list1.print_list()

print('Head:', my_linked_list1.head.value)
print('Tail:', my_linked_list1.tail.value)
print('Length:', my_linked_list1.length)
print('----------------')


                                                                                                                    