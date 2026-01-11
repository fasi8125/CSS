#black jack game


import random
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """takes a list of cards and returns the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return"draw"
    elif computer_score==0:
        return"lose, opponent has black jack"
    elif user_score==0:
        return"win with black jack"
    elif user_score>21:
        return"you went over. you lose"
    elif computer_score>21:
        return"opponent went over. you win"
    elif user_score>computer_score:
        return"you win"
    else:
        return"you lose"
print("welcome to black jack game ")
def play_game():
    user_cards=[]
    computer_cards=[]
    computer_score= -1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())



    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your cards:{user_cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("type'y' to get another card, type'n' to pass: ")
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"your final hand: {user_cards}, final score: {user_score}")
    print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("do you want to play a game of black jack? type 'y' or 'n': ") == "y":
    print("\n"*1)
    play_game() 
            



'''
        # output:
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\10.py"
welcome to black jack game 
do you want to play a game of black jack? type 'y' or 'n': y


your cards:[2, 10], current score: 12
computer's first card: 7
type'y' to get another card, type'n' to pass: y
your cards:[2, 10, 10], current score: 22
computer's first card: 7
your final hand: [2, 10, 10], final score: 22
computer's final hand: [7, 10], final score: 17
you went over. you lose
do you want to play a game of black jack? type 'y' or 'n': y


your cards:[4, 2], current score: 6
computer's first card: 5
type'y' to get another card, type'n' to pass: y
your cards:[4, 2, 10], current score: 16
computer's first card: 5
type'y' to get another card, type'n' to pass: y
your cards:[4, 2, 10, 8], current score: 24
computer's first card: 5
your final hand: [4, 2, 10, 8], final score: 24
computer's final hand: [5, 10, 9], final score: 24
draw
do you want to play a game of black jack? type 'y' or 'n': y


your cards:[5, 5], current score: 10
computer's first card: 4
type'y' to get another card, type'n' to pass: y
your cards:[5, 5, 2], current score: 12
computer's first card: 4
type'y' to get another card, type'n' to pass: y
your cards:[5, 5, 2, 8], current score: 20
computer's first card: 4
type'y' to get another card, type'n' to pass: n
your final hand: [5, 5, 2, 8], final score: 20
computer's final hand: [4, 10, 10], final score: 24
opponent went over. you win
do you want to play a game of black jack? type 'y' or 'n': n
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\10.py"
welcome to black jack game 
do you want to play a game of black jack? type 'y' or 'n': n
PS C:\Users\DELL\CSS> 
'''
