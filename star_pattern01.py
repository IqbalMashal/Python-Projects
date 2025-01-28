

# # Right Triangle Star Pattern
# # *
# # **
# # ***
# # ****
# # *****



print("Enter the character for the pattern: ", end='')
char = input()

print("Enter the number for the pattern: ", end='')
num = int(input())

for i in range(num):
    print(char * (i + 1))  # Print the character repeated (i + 1) times


