#      x
#     xx
#    xxx
#   xxxx
#  xxxxx


print("Enter the character for the pattern: ", end='')
char = input()

print("Enter the number for the pattern: ", end='')
num = int(input())
space = ' '

for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print (space, end='')
    
    print (char * (num-i+1))
