# debugging code
def odd_or_even(number):
    if number % 2 == 0: # the error is they(=)is mention not (==)
        return "This is an even number."
    else:
        return "This is an odd number."
print(odd_or_even(12))

# output 
# PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\12.py"
#This is an even number
#
    

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:# in leap year the % is divide by 400 not 4000
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print (is_leap(year=2024))



def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

print(fizz_buzz(5))

# output
#  #PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\12.py"
# # 1
# 2
# Fizz
# 4
# Buzz
# None