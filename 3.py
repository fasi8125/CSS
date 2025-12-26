print("Welcome to the treasure island ")
print("your mission is to find the treasure")

choice1 = input('you\'re at a cross road .where do u want to go? type "left" or "right:"').lower()

if choice1=="left":
    choice2 = input('you \'ve come to a lake .there is an island in the middle of the lake.type "wait" to wait for a boat .type "swim" to swim across:').lower()
     
     
    if choice2=="wait":
            choice3=input("you have arrived at the island unharmed .there is a house with 3 doors .one red ,one yellow and one blue.which colour do u choose?").lower()
            if choice3=="red":
                print("it is full of fire .game over")
            elif choice3=="yellow":
                print("you find the treasure! you win!")
            elif choice3=="blue":
                print("you enter the room of beasts.game over")
    else:
          print("you got attacked by an angry trout .game over")

else:
       print("you have fell into a hole .game over")