print("what do you choose? type 0 for rock ,1 for scissors and 2 for papper")
user_choice=int(input("choose a number b/w 0-2:"))
import random
computer_choice=random.randint(0,2)
print(f"computer chose {computer_choice}")
if user_choice == computer_choice:
    print("its a draw")
elif(user_choice==0 and computer_choice==1)or (user_choice==1 and computer_choice==2)or (user_choice==2 and computer_choice==0):
    print(" congratulation! you win")
elif(user_choice==0 and computer_choice==2)or (user_choice==1 and computer_choice==0)or (user_choice==2 and computer_choice==1):
    print("you lose")
else:
    print("invalid input! you lose")

    '''
    
    #output:

    PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\3.py"
what do you choose? type 0 for rock ,1 for scissors and 2 for papper
choose a number b/w 0-2:1
computer chose 1
its a draw
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\3.py"
what do you choose? type 0 for rock ,1 for scissors and 2 for papper
choose a number b/w 0-2:2
computer chose 0
 congratulation! you win
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\3.py"
what do you choose? type 0 for rock ,1 for scissors and 2 for papper
choose a number b/w 0-2:0
computer chose 2
you lose
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\3.py"
what do you choose? type 0 for rock ,1 for scissors and 2 for papper
choose a number b/w 0-2:3
computer chose 2
invalid input! you lose
PS C:\Users\DELL\CSS> '''