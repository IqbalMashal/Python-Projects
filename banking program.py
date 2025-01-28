


def show_Balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("Invalid amount")
        return 0

    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount you want to withdraw: "))
    if amount > balance:
        print(f"The amount ${amount:.2f} which greater than the current balance ${balance:.2f}")
        return 0
    elif amount <= 0:
        print("Invalid amount")
        return 0
    else:
        return amount
    


def main():

    balance = 0

    is_running = True


    while is_running:

        print(20 * '*')
        print("   Banking Program")
        print(20 * '*')

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print ("4. Exit")
        print(20 * '*')


        choice = input("Enter yous choice (1-4): ")
        choice = int(choice)

        if choice == 1:
            show_Balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print(20 * '*')
            print("\nInvalid choice, try again")
            print("\n")


    print("Thank you have a nice day!")


if __name__ == '__main__':
    main()

