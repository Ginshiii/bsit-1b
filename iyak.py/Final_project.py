def print_():
  print("the print() function is used to output data to the console or standard output device. It can display various types of data such as strings, numbers, lists, or even complex data structures. The print() function can also handle multiple arguments and automatically converts them to strings before printing.")

  print('''# Printing a simple string
  print("Hello, World!")
  ''')

def Variables_and_Data_Types():
  print("variables are created by simply assigning a value to them. Python has various data types such as integers, floating-point numbers, strings, lists, and more")

  print('''  # Assigning variables
  x = 5        # Integer
  y = 3.14     # Floating point number
  name = "John" # String
  is_active = True # Boolean

  # Printing the variables
  print(x)      # Output: 5
  print(y)      # Output: 3.14
  print(name)   # Output: John
  print(is_active) # Output: True''')

def Indentation():
  print("Python uses indentation to define blocks of code, rather than braces {} like other programming languages. This is one of Python's most unique features")

  print('''if x > 0:
    print("x is positive")  # This block is executed if condition is True
  else:
      print("x is non-positive")  # This block runs if the condition is False
  ''')

def if_else():
  print("Python uses if, elif, and else to make decisions based on conditions.")

  print('''age = 20

  if age < 18:
      print("You are a minor")
  elif age >= 18 and age < 65:
      print("You are an adult")
  else:
      print("You are a senior citizen")
  ''')

def for_loop():
  print("The for loop is typically used to iterate over a sequence (like a list or a string).")

  print('''# Iterating over a list of numbers
  for i in range(5):
      print(i)
  0
  1
  2
  3
  4

  ''')
def while_loop():
  print("The while loop runs as long as a condition is True.")

  print('''counter = 0
  while counter < 5:
      print(counter)
      counter += 1
    0
    1
    2
    3
    4


    ''')

def function():
  print("Functions in Python are defined using the def keyword.")

  print('''def greet(name):
    return f"Hello, {name}!"

  # Calling the function
  print(greet("Alice"))
  Output...... Hello, Alice!
  ''')

def lists():
  print("Lists in Python are ordered collections that can hold multiple items.")

  print('''# Creating an initial list
  fruits = ['apple', 'banana', 'cherry']

  # Using append() to add a new item
  fruits.append('orange')

  # Printing the updated list
  print(fruits)
  ['apple', 'banana', 'cherry', 'orange']

  ''')

def dictionaries():
  print("Dictionaries in Python store data in key-value pairs.")

  print('''person = {"name": "John", "age": 30, "city": "New York"}

  # Accessing values by key
  print(person["name"])  # Output: John

  # Adding a new key-value pair
  person["job"] = "Engineer"
  print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
  ''')

def comments():
  print(" comments are written with the # symbol. They help explain the code but are not executed.")

  print(" # sir mesiera pogi ahhahhahahah")

def math_operators():
  print('''the following operators are used for mathematical operations:

  + (Addition)
  - (Subtraction)
  * (Multiplication)
  / (Division)
  % (Modulus)
  ** (Exponentiation)
  // (Floor Division)''')

def assignment_operators():
  print('''assignment operators are used to assign values to variables. These operators allow you to assign a value to a variable, and in some cases, modify the value in a specific way during the assignment. Python has several assignment operators, each performing different types of assignments or updates to a variable.

  Basic Assignment Operator: =
  The basic assignment operator (=) assigns the value on the right-hand side to the variable on the left-hand side.''')

  print('''x = 5
  x -= 2  # Equivalent to x = x - 2
  print(x)  # Output: 3
  ''')


x = True

while x:
  print("-------------------------------")
  print("WELCOME TO MY COMPILATION PROGRAM")

  print("PLEASE SELECT FROM THE OPTIONS BELOW")
  print("1 -- Print")
  print("2 -- Variables and Data Types")
  print("3 -- Comments  ")
  print("4 -- Indentation")
  print("5 -- If Else Elif")
  print("6 -- For Loop ")
  print("7 -- While Loop")
  print("8 -- Function ")
  print("9 -- Lists")
  print("10 -- Dictionaries")
  print("11 -- Math Operators")
  print("12 -- Assignment Operator")
  print("13 -- Exit:)")

  choice = eval(input("Which program would you like to run (1 - 11) -- > "))

  if choice == 1:
    print_()

  elif choice == 2:
    Variables_and_Data_Types()

  elif choice == 3:
    comments()

  elif choice == 4:
    Indentation()

  elif choice == 5:
    if_else()

  elif choice == 6:
    for_loop()

  elif choice == 7:
    while_loop()

  elif choice == 8:
    function()

  elif choice == 9:
    lists()

  elif choice == 10:
    dictionaries()

  elif choice == 11:
    math_operators()

  elif choice == 12:
    assignment_operators()

  elif choice == 13:
    print(" Stop na")
    break
  
  else:
    print("Invalid Choice")
    continue