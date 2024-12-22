name = input("enter your name:")
missu1 = eval(input("Enter your deposit: "))
print("Hi!" ,name, " your deposit amount breakdown in PH denominator is as follow" )

missu2 = missu1 // 1000
missu3 = missu1 % 1000

print(missu2, "1000")

missu4 = missu3 // 500
missu5 = missu3 % 500


print(missu4, "500")

missu6 = missu5 // 200
missu7 = missu5 % 200

print (missu6, "200")

missu8 = missu7 // 100
missu9 = missu7 % 100

missu10 = missu9 // 50
missu11 = missu9 % 50

print(missu8, "100")
print(missu10, "50")

missu12 = missu11 // 20
missu13 = missu11 % 20

missu14 = missu13 // 10
missu15 = missu13 % 10

missu16 = missu15 // 5
missu17 = missu15 % 5

missu18 = missu17 // 1
missu19 = missu17 % 1

print(missu12, "20")
print(missu14, "10")
print(missu16, "5")
print(missu18, "1")