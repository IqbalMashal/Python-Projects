


def partial_sum(my_list: list, length: int) -> int:
    if length == 0:
        return 0
    return my_list[length - 1] + partial_sum(my_list, length - 1)

arr = [4, 2, 5, 7, 6]
size = len(arr)
sum_result = partial_sum(arr, size)
print(sum_result)

def check_binary(my_list, left, right, key):
    if left > right:
        return False
    mid = (left + right) // 2
    if key > my_list[mid]:
        return check_binary(my_list, mid + 1, right, key)
    elif key < my_list[mid]:
        return check_binary(my_list, left, mid - 1, key)
    else:
        return mid

def binary(my_list, key):
    return check_binary(my_list, 0, len(my_list) - 1, key)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary(arr, 5)
print(index)

def sum_of_digits(n):
    if n >= 0 and n <= 9:
        return n
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))

def find_max(my_list, start, end):
    if start == end:
        return my_list[start]
    mid = (start + end) // 2
    max1 = find_max(my_list, start, mid)
    max2 = find_max(my_list, mid + 1, end)
    return max1 if max1 > max2 else max2

def find_min(my_list, start, end):
    if start == end:
        return my_list[start]
    mid = (start + end) // 2
    min1 = find_min(my_list, start, mid)
    min2 = find_min(my_list, mid + 1, end)
    return min1 if min1 < min2 else min2

arr = [5, 3, 6, 52, 8, 9]
max_result = find_max(arr, 0, len(arr) - 1)
print(max_result)

def reverse_string(my_str, start, end):
    if start >= end:
        return ''.join(my_str)
    my_str[start], my_str[end] = my_str[end], my_str[start]
    return reverse_string(my_str, start + 1, end - 1)

text = 'Hello'
text_list = list(text)
print(reverse_string(text_list, 0, len(text_list) - 1))

def power(b, e):
    if e == 0:
        return 1
    return b * power(b, e - 1)

def main():
    b = int(input("Input the base number: "))
    e = int(input("Input the exponent: "))
    result = power(b, e)
    print(f"{b} raised to the power of {e} is: {result}")

if __name__ == "__main__":
    main()

def palindrome(my_list, start, end):
    if start > end:
        return True
    if my_list[start] != my_list[end]:
        return False
    return palindrome(my_list, start + 1, end - 1)

text = 'dad'
print(palindrome(list(text), 0, len(text) - 1))

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(current, previous=None):
    if current is None:
        return previous
    next_node = current.next
    current.next = previous
    return reverse_list(next_node, current)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    return gcd(y, x % y)

def calculate_even_odd_sum(start, end, even_sum=0, odd_sum=0):
    if start > end:
        return even_sum, odd_sum
    if start % 2 == 0:
        even_sum += start
    else:
        odd_sum += start
    return calculate_even_odd_sum(start + 1, end, even_sum, odd_sum)
