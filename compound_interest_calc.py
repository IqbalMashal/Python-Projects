principal = 0
rate = 0
time = 0

# Input validation for principal
while principal <= 0:
    try:
        principal = float(input("Enter the principal amount: "))
        if principal <= 0:
            print("Principal cannot be less than or equal to zero.")
    except ValueError:
        print("Please enter a valid number for the principal.")

# Input validation for rate
while rate <= 0:
    try:
        rate = float(input("Enter the interest rate: "))
        if rate <= 0:
            print("Interest rate cannot be less than or equal to zero.")
    except ValueError:
        print("Please enter a valid number for the interest rate.")

# Input validation for time
while time <= 0:
    try:
        time = int(input("Enter the time period in years: "))
        if time <= 0:
            print("Time cannot be less than or equal to zero.")
    except ValueError:
        print("Please enter a valid number for the time period.")

# Calculating total amount after applying interest
total = principal * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")
