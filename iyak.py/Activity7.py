#activity7
#SCHOLAR GRANT APLICATION SYSTEM

name = input("Hi please enter your name:")
Enrolled = input("Are you curently enrolled in DLL (yes / no):")

if Enrolled.lower() == "yes":
  #is student age 18 to 35
  print(f"Hi, {name}. Welcome to DLL Scholar Grant Syetem.")
  age = eval(input("How old are you right now? "))

  if age >= 18 and age <= 35: 
    print("Your age compied with the age requirment.")
    grade = eval(input("What was your last GWA?"))

    if grade >= 86 and grade <= 100: 
      print("your grades pass the requirment")
      is4ps = input("is your family currently enrolled in 4ps program? ")

      if is4ps.lower() == "yes":
        print(f"congratulations {name}! you are now granted a scholarship")

      else:
        print("sorry for 4ps member only")

    else:
      print("sorry you are not eligible for the scholarship")

  else:
    print("sorry")
else:
  print("Thank you for using the system")