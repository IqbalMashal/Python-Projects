from art import logo, vs
from game_data import data
import random
print(logo.center(100))

print("Welcome to the High or Low game!")
print("You will be given two femouse personalities.")
print("You have to gusse which one has more followers on Instagram.")


def get_random_person():

    celebrity1 = random.choice(data)
    celebrity2 = random.choice(data)
    if celebrity1 == celebrity2:
        celebrity2 = random.choice(data)
    
    return celebrity1, celebrity2

def get_person_info(celebrity):
    name = celebrity["name"]
    description = celebrity["description"]
    country = celebrity["country"]
    return f"{name}, a {description}, from {country}"

def get_person_followers(celebrity):
    return celebrity["follower_count"]

def compare_followers(celebrity1, celebrity2):
    followers1 = get_person_followers(celebrity1)
    followers2 = get_person_followers(celebrity2)
    return followers1 > followers2  

def game():
    score = 0
    game_continue = True
    while game_continue:
        celebrity1, celebrity2 = get_random_person()
        print('\n'*2)
        print('*'*100)
        print(f"Compare A: {get_person_info(celebrity1)}")
        print(vs.center(100))
        print(f"Against B: {get_person_info(celebrity2)}")
        print('*'*100)
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if compare_followers(celebrity1, celebrity2):
            correct_answer = 'a'
        else:
            correct_answer = 'b'
        if guess == correct_answer:
            score += 1
            print(f"Correct! Your current score is: {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Your final score is: {score}")

game()
