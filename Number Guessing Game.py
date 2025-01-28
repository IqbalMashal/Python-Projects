import random

lowest_num  = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True


print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses+=1

        if guess > highest_num or guess < lowest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print ("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try agnin!")
        else:
            print(f"Correct! the answer was {answer}")
            print(f"It took you {guesses} number of guesses")
            is_running = False
    
    else:
        print("Inavlid geuss")  
        print(f"Please select a number between {lowest_num} and {highest_num}")
