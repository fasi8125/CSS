print("weloome to the password generator ")
nr_length=int(input("what length u want the passworrd to be?"))
print(nr_length)
nr_numbers=int(input("how many numbers u want in the password?"))
print(nr_numbers)
nr_symbols=int(input("how many symbols would u want in the password?"))
print(nr_symbols)
symbols=['!','@','#','$','%','^','&','*','(',')','-','+']
numbers=['0','1','2','3','4','5','6','7','8','9']
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
import random
password_list=[]

for char in range(1,nr_length+1):
    password_list += random.choice(letters)
for char in range(1,nr_numbers+1):
    password_list  += random.choice(numbers)
for char in range(1,nr_symbols+1):
    password_list += random.choice(symbols)   




password=""
random.shuffle(password_list)
for char in password_list:
    password += char    
print(f"your password is:{password}")
'''
#output:

# PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\4.py"
weloome to the password generator
what length u want the passworrd to be?4
4
how many numbers u want in the password?5
5
how many symbols would u want in the password?6
6
your password is:sKwO74706**#!-^
PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\4.py"
weloome to the password generator
what length u want the passworrd to be?3
3
how many numbers u want in the password?3
3
how many symbols would u want in the password?3
3
your password is:1&P26!qg#
PS C:\Users\DELL\CSS>'''