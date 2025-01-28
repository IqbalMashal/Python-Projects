


# * * * * *
# * * * *
# * * *
# * *
# *

print("Enter the character for the pattern: ", end='')
char = input()

print("Enter the number for the pattern: ", end='')
num = int(input())

for i in range(num, 0, -1):
    print(char * i)
