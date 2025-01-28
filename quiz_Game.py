

# Tuples and lists in Python are both used to store collections of items, but they have some key differences. Here are a few examples highlighting where they differ:
# 1. Immutability:

#     Tuple: Cannot be modified after creation.
#     List: Can be modified (elements can be added, removed, or changed).
# # Tuple methods
# my_tuple = (1, 2, 3, 2)
# print(my_tuple.count(2))  # Output: 2 (Counts occurrences of 2)
# print(my_tuple.index(3))  # Output: 2 (Finds index of 3)

# # List methods
# my_list = [1, 2, 3]
# my_list.append(4)  # Adds 4 to the end of the list
# print(my_list)     # Output: [1, 2, 3, 4]
# my_list.remove(2)  # Removes the first occurrence of 2
# print(my_list)     # Output: [1, 3, 4]



questions = (
    "What planet is known as the 'Red Planet'?",
    "What is the process by which plants make their own food using sunlight called?",
    "Which gas do humans need to breathe in to survive?",
    "What is the force that pulls objects toward the center of the Earth?",
    "What is the chemical formula for water?"
)

# Fixed options tuple with meaningful choices
options = (
    ("A. Earth", "B. Mars", "C. Venus", "D. Jupiter"),
    ("A. Respiration", "B. Transpiration", "C. Photosynthesis", "D. Germination"),
    ("A. Carbon Dioxide", "B. Hydrogen", "C. Oxygen", "D. Nitrogen"),
    ("A. Friction", "B. Magnetism", "C. Gravity", "D. Tension"),
    ("A. CO2", "B. H2O", "C. O2", "D. NaCl")
)

answers = (
    "B. Mars", 
    "C. Photosynthesis", 
    "C. Oxygen", 
    "C. Gravity", 
    "B. H2O"
)

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()

    # Validate the input to ensure it's one of the valid options
    while guess not in ('A', 'B', 'C', 'D'):
        guess = input("Invalid choice. Please enter A, B, C, or D: ").upper()

    guesses.append(guess)

    # Check only the first character of the answer, not the entire string
    if guess == answers[question_num][0]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

# Optional: Print the final score at the end
print(f"\nYour final score is: {score}/{len(questions)}")
