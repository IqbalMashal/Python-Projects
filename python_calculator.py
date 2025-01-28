<<<<<<< HEAD



operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 
else:
    print(f"{operator} is not a valid operator")
# f-string (f"{operator} is not a valid operator"): 
# This is a formatted string literal (f-string) that allows 
# you to embed expressions inside string literals using curly braces {}.

=======



operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 
else:
    print(f"{operator} is not a valid operator")
# f-string (f"{operator} is not a valid operator"): 
# This is a formatted string literal (f-string) that allows 
# you to embed expressions inside string literals using curly braces {}.

>>>>>>> e2bd696e94f1942a572e38fc28799ddbb567149b
print (round(result,2))