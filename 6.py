word_list=["apple","banana","cherry"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("guess a letter:").lower()
print(guess)
for letter in chosen_word:
    if guess==letter:
        print("right")
    else:
        print("wrong")
'''
#output:
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\6.py"
banana
guess a letter:a
a
wrong
right
wrong
wrong
right
wrong
right
'''








import random
word_list=["apple","grapes","cherry"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)
guess = input("guess a letter:").lower()
print(guess)
display=""
for letter in chosen_word:
    if letter==guess:
        display+=letter
    else:
        display+="_"
print(display)
''''
#output:
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\6.py"
apple
_____
guess a letter:w
w
_____
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\6.py"
cherry
______
guess a letter:r
r
___rr_
'''