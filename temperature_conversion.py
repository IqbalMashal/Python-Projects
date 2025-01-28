<<<<<<< HEAD


unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

temp = float(input("Enter the temperature: "))


if unit == "C":
    tempResult = round((9 * temp) / 5 + 32, 1)
    unit = "celsius"
elif unit == "F":
    tempResult = round((temp - 32) * 5/9, 1)
else: 
    print(f"{unit} is not a valid option")

=======


unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

temp = float(input("Enter the temperature: "))


if unit == "C":
    tempResult = round((9 * temp) / 5 + 32, 1)
    unit = "celsius"
elif unit == "F":
    tempResult = round((temp - 32) * 5/9, 1)
else: 
    print(f"{unit} is not a valid option")

>>>>>>> e2bd696e94f1942a572e38fc28799ddbb567149b
print(f"The temperature in {unit} is {tempResult}")