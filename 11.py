import random

easy_level_attempts = 10
hard_level_attempts = 5


def check_answer(user_guess, actual_number, turns):
    if user_guess < actual_number:
        print("Too low")
        return turns - 1
    elif user_guess > actual_number:
        print("Too high")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_number}")
        return turns


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return easy_level_attempts
    else:
        return hard_level_attempts


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
# print(f"(DEBUG) Correct answer is {number}")

turns = set_difficulty()

guess = 0
while guess != number and turns > 0:
    print(f"You have {turns} attempts remaining.")
    guess = int(input("Make a guess: "))

    turns = check_answer(guess, number, turns)

    if turns == 0:
        print(f"You've run out of guesses. You lose! The correct number was {number}.")
    elif guess != number:
        print("Guess again.")


    

# ''' hard level output example:

# PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\11.py"
# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Choose a difficulty. Type 'easy' or 'hard': hard
# You have 5 attempts remaining.
# Make a guess: 56
# Too high
# Guess again.
# You have 4 attempts remaining.
# Make a guess: 40
# Too high
# Guess again.
# You have 3 attempts remaining.
# Make a guess: 30
# Too high
# Guess again.
# You have 2 attempts remaining.
# Make a guess: 23
# Too low
# Guess again.
# You have 1 attempts remaining.
# Make a guess: 27
# Too low
# You've run out of guesses. You lose! The correct number was 29.
# PS C:\Users\DELL\CSS> 
# '''

''' # easy level output example:
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\11.py"
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining.
Make a guess: 45
Too low
Guess again.
You have 9 attempts remaining.
Make a guess: 78 
Too high
Guess again.
You have 8 attempts remaining.
Make a guess: 67
Too low
Guess again.
You have 7 attempts remaining.
Make a guess: 75
Too low
Guess again.
You have 6 attempts remaining.
Make a guess: 76
You got it! The answer was 76
PS C:\Users\DELL\CSS> 
'''