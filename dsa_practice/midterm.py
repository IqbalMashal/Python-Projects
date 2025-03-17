# Everything in Python is an object, and variables store references (not actual values).
# Immutable objects (int, str, tuple) create a new object when changed.
# Mutable objects (list, dict, set) modify the same object in memory.
# You can use id() to check if two variables point to the same object.

# Q1:

# What is the run time of the following function:

# def f1(number):
#     rc = 1    1 opration for (=) 

#     for i in range(0, 5): 1 + 5 1 for range function and 5 for the numbers of itrations done by the function
# 
#         rc += 1   1(5) for += and and (5) becuase this operation is going to happen 5 times 
#     return rc 1 for the return fucntuin




# Q2:

# What is the run time of the following function:

# def f1(n):
#     rc = 1
#     i = 0
#     while i < n:
#         rc += 1
#         i += 2
#     return rc

# Q3:

# Suppose that the function g1(n) has a run time of O(n) and g2(n) has a run time of O(n^2) What is the run time of f1(n)?

# def f1(n):
#     g1(n)
#     g2(n)

# Q4:

# Write the following function recursively:

# def is_palindrome(word)


def is_palindrome(word):
    pass
    

    def check_palindrome(my_word, start, end):
        if start > end:
            return True
        if my_word[start] != my_word[end]:
            return False
        
        return check_palindrome(my_word, start+1, end-1)

    return check_palindrome(word.lower(), 0, len(word)-1)


word = 'Dad'
# print(is_palindrome(word))


# word is a character string. This function returns true if word is a palindrome. A palindrome is a string that reads the same forwards and backwards. Thus: noon, mom, dad are all palindromes. table, texture, glass are not palindromes.

# the above function can be a wrapper to a function that actually does the work

# Try to write the function to O(n) run time where n is the length of s.
# Q5:

# When using a singly linked list to implement a stack, is it better for insertions to occur at the front or back of the list (or does it matter)? Why?
# Q6:

    # it honestly doesn't matter in which order we insert what matters is that we should alway remove or delete the most recent or newest element that was pushed into the stack via a linked list
    # although generally as stack is a FILO data strcture it is better and easy to understant that we should insert at the front of the linked list as most of the time we only have access to the head or front of the linked list and insertion will take as O(1)
    # where if we don't know where the back is or don;t have access to it, it will take us O(n) to travers to the linked list and find the back and insert values into it
# The following show a table of keys and the hash index of these keys within a table of size 10

# key 	hashIdx
# alpha 	8
# beta 	9
# gamma 	8
# apple 	4
# orange 	4
# cherry 	5
# part a

# Draw an empty array of size 10 that represents a linear probing table.
# part b

# Insert the keys in the following order and show the final array:

#     beta
#     alpha
#     gamma
#     apple
#     cherry
#     orange

# part c

# remove apple from table in part b, what does final array look like
# part d

# remove beta from table in part c, what does final array look like
# part e

# If you used tombstones in the previous parts, redo this question (parts A to D) without tombstones. If you did it without tombstones, redo this question (parts A to D) with tombstones
# Q7:

# Describe what you will need to implement a queue using an array such that you have O(1) runtimes for enqueue() and dequeue() operations. Do this WITHOUT using code (ie what do you need, why do you need it, but don't just code dump)
# Q8:

# A self adjusting linked list is a linked list where a successful search causes the list to adjust so that the found item is moved to the front (and thus allowing successive search for same item to be more readily found).

# Given the following class declarations for a doubly linked self adjusting linked list:

# class SelfAdjustingList:
# 	class Node:
# 		def __init__(self, dat, nx, pr):
# 			self.data = dat
# 			self.next = nx
# 			self.prev = pr

# 	def __init__(self, id_list):
#                 self.front = ...
#                 self.back = ...

# Write the following function:

# def search(self, v)

#     This function searches for v within the list and returns true if v is found. If not found, function returns false
#     The list will be adjusted so that the found node is moved so that it becomes the first data node in the list
#     Function must have run time of O(n)
#     Implement two versions of this, one using sentinels and one without.

# Q9: Recursive Analysis:

# Perform an analysis on do_something() function with respect to the length of the string str

# def do_recursion(str, curr):
#     if curr == len(str):
#         return 0
#     elif str[curr] == "a":
#         return 1 + do_recursion(str, curr + 1)
#     else:
#         return do_recursion(str, curr + 1)

# def do_something(str):
#     return do_recursion(str, 0)


# print(False == [])


# x = 5
# y = x
# y = 7

# print(f"y {y} and x {x}")



# list1 = [1,2,3,4]
# list2 = list1
# list2[1] = 50
# print(list1)  # output: [1, 50, 3, 4]

# x = [0,0,0]

# y = [x,x,x]

# print(y)

# y[1][1] = 1

# print(y)


# [0,1,0],[0,1,0],[0,1,0]


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age  # Attributes can be modified later

# # Creating an object
# p1 = Person("Alice", 25)

# # Modifying an attribute (allowed)
# x = p1.age = 30 

# x = 70

# print(p1.age)  # Output: 30



class Stack:
    def __init__(self, size = 10):
        self.stack = []
        self.lenght = 0
    def push(self,data):
        self.stack.append(data)
        self.lenght+=1
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[0]
    def isEmpty(self):
        return False if self.lenght == 0 else True
    def isFull(self):
        pass


# Stack Implementations
# Implementation	Push (Add)	Pop (Remove)	Top (Access)
# Array (Back of Array)	O(1)	O(1)	O(1)
# Array (Front of Array)	O(n) (Shift all elements)	O(1)	O(1)
# Linked List (Front of List)	O(1)	O(1)	O(1)
# Linked List (Back of List w/o tail pointer)	O(n)	O(n)	O(n)

# ✅ Best Choice:

#     Use linked list (front insertion and removal)
#         Push: Insert at the front → O(1)
#         Pop: Remove from the front → O(1)
#         Top: Access the front → O(1)

# Queue Implementations
# Implementation	Enqueue (Add)	Dequeue (Remove)	Front (Access)
# Array (Front Insertion, Back Removal)	O(n)	O(1)	O(1)
# Array (Back Insertion, Front Removal)	O(1)	O(n)	O(1)
# Circular Array	O(1)	O(1)	O(1)
# Linked List (Front Insertion, Back Removal, No Tail Pointer)	O(1)	O(n)	O(n)
# Linked List (Back Insertion, Front Removal, With Tail Pointer)	O(1)	O(1)	O(1)

# ✅ Best Choice:

#     Use linked list (back insertion, front removal, with tail pointer)
#         Enqueue: Insert at the back → O(1)
#         Dequeue: Remove from the front → O(1)
#         Front: Access the front → O(1)

# Summary of Best Implementations
# Data Structure	Best Approach
# Stack	Linked List (Front Insert, Front Remove)
# Queue	Linked List (Back Insert, Front Remove) w/ Tail Pointer
# Queue (Array Version)	Circular Array for O(1) Operations

# These implementations ensure constant-time operations (O(1)) wherever possible. 🚀




