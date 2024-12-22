 #for loop
for x in range(1, 6):

  for z in range(1, 6):

    for y in range(1, x +1):

      print("*",end=" ")

    for a in range(6, x, -1):
       print("",end="")

    print(end="")

  print()