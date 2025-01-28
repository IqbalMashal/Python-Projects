menu = {
    "Burger": 5.99,
    "Pizza": 8.49,
    "Fries": 2.99,
    "Sandwich": 4.49,
    "Taco": 3.99,
    "Salad": 4.99,
    "Soda": 1.99,
    "Coffee": 2.49,
    "Ice Cream": 3.49,
    "Hot Dog": 3.29
}

cart = []
total = 0

# Display the menu
print("-------------- Menu -----------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-------------------------------------")

# Taking user input
while True:
    food = input("Select an item (q to quit): ").title()  # Title case for consistent matching
    if food == 'Q':
        break
    elif food in menu:
        cart.append(food)
    else:
        print("Item not available. Please select from the menu.")

# Display the order and calculate the total
print("\n-------------- Your Order -----------------")
for food in cart:
    total += menu.get(food)
    print(food)

print()
print(f"Total is: ${total:.2f}")
