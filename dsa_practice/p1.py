def reverse_number(num):
    if num <= 0:
        print("incorrect number")
    
    temp = num
    last_digit = 0
    reverse_num = 0
    
    while temp != 0:
        last_digit = temp % 10
        reverse_num = reverse_num * 10 + last_digit 
        temp = temp// 10
    
    return reverse_num

print(reverse_number(1234))