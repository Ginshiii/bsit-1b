#Built in functions 
#input(), type(), print(), len(), int(), evalu(), float(), lower(), upper(), str(),

#Programmer - defined functions 

#def function_name(parameters):
#   code block  

#creation of function
def greet_Someone():
    print("Hi , hoped your having a delightful Tuesday afternoon.")


def greet_Person(name):
    print(f"Hi {name}, hoped your having a delightful Tuesday afternoon.")

def right_Triangle():
    for x in range(1, 6):
        for y in range(1, x+1):
            print("*", end=" ")
        for z in range(6, x, -1):
            print(" ",end= " ")
        print()

def get_info(name, age):
    print(f"Hi {name}, with age {age} yrs old.")


def factorial(number):
    #factorial of 4 - 4 x 3 x 2 x 1 
    fact = 1 
    for x in range(number, 0, -1):
        fact *= x
    print(f"The factorial of {number} is {fact}")



tuloy = True

while tuloy:
    print("-------------------------------")
    print("WELCOME TO MY COMPILATION PROGRAM")

    print("PLEASE SELECT FROM THE OPTIONS BELOW")
    print("1 -- RIGHT TRIANGLE")
    print("2 -- FACTORIAL")
    print("3 -- GREET SOMEONE")
    print("4 -- EXIT")

    choice = eval(input("Which program would you like to run (1,2,3,4) -- > "))

    if choice == 1:
        print("THIS IS A PROGRAM THAT WILL SHOW YOU A RIGHT TRIANGLE MADE FROM PYTHON")
        right_Triangle()
        continue
    elif choice == 2:
        print("THIS IS A PROGRAM THAT CALCULATES FACTORIAL")
        number = eval(input("enter a number "))
        factorial(number)
        continue
    elif choice == 3:
        greet_Someone()
        continue
    elif choice == 4:
        print("Program Terminated")
        break
    else:
        print("INVALID CHOICE")
        continue
