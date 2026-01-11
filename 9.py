#simple calculator app which perform basic arithmetic operations


def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def power(n1,n2):
    return n1**n2
def mod(n1,n2):
    return n1%n2
def floor_divide(n1,n2):
    return n1//n2
operations ={"+":add
             ,"-":subtract
              ,"*":multiply
              ,"/":divide
              ,"**":power
              ,"%":mod
              ,"//":floor_divide
              }
def calculator():
    should_continue=True
    print("welcome to the calculator app")

    number1=float(input("enter the first number:" ))

    while should_continue:
      for symbols in operations:
        print(symbols)
      operations_symbols= input("enter the operation you want to perform:" )
      number2=float(input("enter the second number:" ))
      answer=operations[operations_symbols](number1,number2)
      print(f"{number1} {operations_symbols} {number2} = {answer}")
      choice=input(f"type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
      if choice=="y":
        number1=answer
      else:
        should_continue=False
        print("\n"*1)
        print("thank you for using the calculator ")
calculator()

#output:
# PS C:\Users\DELL\CSS> python -u "c:\Users\DELL\CSS\9.py"
# welcome to the calculator app
# enter the first number:10
# +
# -
# /
# **
# %
# //
# enter the operation you want to perform:+
# enter the second number:5
# 10.0 + 5.0 = 15.0
# type 'y' to continue calculating with 15.0, or type 'n' to exit: y
# +
# -
# *
# /
# **
# %
# //
# enter the operation you want to perform:/
# enter the second number:2
# 15.0 / 2.0 = 7.5
# type 'y' to continue calculating with 7.5, or type 'n' to exit: y
# +
# -
# *
# /
# **
# %
# //
# enter the operation you want to perform:*
# enter the second number:5
# 7.5 * 5.0 = 37.5
# type 'y' to continue calculating with 37.5, or type 'n' to exit: y
# +
# -
# *
# /
# **
# %
# //
# enter the operation you want to perform://
# enter the second number:2
# 37.5 // 2.0 = 18.0
# type 'y' to continue calculating with 18.0, or type 'n' to exit: y
# +
# -
# *
# /
# **
# %
# //
# enter the operation you want to perform:**
# enter the second number:2
# 18.0 ** 2.0 = 324.0
# type 'y' to continue calculating with 324.0, or type 'n' to exit: y
# +
# -
# *
# /
# **
# %
# //
# enter the operation you want to perform:%
# enter the second number:5
# 324.0 % 5.0 = 4.0
# type 'y' to continue calculating with 4.0, or type 'n' to exit: -


# thank you for using the calculator
# PS C:\Users\DELL\CSS> 