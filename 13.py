import random
import os

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

logo = """
__  ___       __             
/ / / (_)___ _/ /_  ___  _____
/ /_/ / / __ '/ __ \\/ _ \\/ ___/
/ __  / / /_/ / / / /  __/ /    
/_/ ///_/\\__, /_/ /_/\\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {"name": "Instagram", "follower_count": 346, "description": "Social media platform", "country": "United States"},
    {"name": "Cristiano Ronaldo", "follower_count": 215, "description": "Footballer", "country": "Portugal"},
    {"name": "Ariana Grande", "follower_count": 183, "description": "Musician and actress", "country": "United States"},
    {"name": "Virat Kohli", "follower_count": 55, "description": "Cricketer", "country": "India"},
    {"name": "NASA", "follower_count": 56, "description": "Space agency", "country": "United States"},
    {"name": "NBA", "follower_count": 47, "description": "Basketball league", "country": "United States"},
]

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    score = 0
    account_a = random.choice(data)
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    while True:
        clear()
        print(logo)
        print(f"Score: {score}")
        print()
        print("Compare A:", format_data(account_a))
        print(vs)
        print("Against B:", format_data(account_b))

        guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        if guess not in ["a", "b"]:
            print("❌ Invalid input! Please type A or B.")
            input("Press Enter to continue...")
            continue

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            account_a = account_b
            account_b = random.choice(data)

            while account_a == account_b:
                account_b = random.choice(data)
        else:
            clear()
            print(logo)
            print(f"❌ Sorry, that's wrong.")
            print(f"🏁 Final Score: {score}")
            break

# Run game
game()
