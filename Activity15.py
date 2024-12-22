d = True
nt = 0
while d == True :
    ask = input ("Do you wish to print triangles (yes or no ):")

    if ask.lower() == "no":
      print("Loop has Ended")
      break
      d = False

    elif ask.lower() == "yes":
      nt += 1
      for x in range(1, 6):
        for r in range(1, nt + 1):
          for y in range(1,x + 1):
            print("*", end=" ")
          for z in range (6, x, -1):
            print(" ", end=" ")
          print(end=" ")
        print()
      continue 
    else:
      print("INVALID")
      continue
