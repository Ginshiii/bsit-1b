num = eval(input("Enter the number of columns: "))

for x in range(1,num):

  for y in range(1, num + 1):
    print(f"{x} * {y} = {x * y}",end="\t")

  print()