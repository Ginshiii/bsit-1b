#WHILE LOOP 
#TYPES OF LOOP 
#FOR LOOP - use if you have certain or definite amout of times to repeart a code block 
#WHILE LOOP - use if you are uncertain on the amount of times to repeat a code block 

#boolean variable / trigger 

n = True

sum = 0
while n == True:
  num = eval(input("Enter any number --->  "))

  if num == 0:
    print("LOOP STOPPED")
    print(f"The sum of all the numbers given is {sum}")
    break
    n = False 
  else:
    sum += num 
    continue