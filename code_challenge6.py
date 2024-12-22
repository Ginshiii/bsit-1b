name = input("Enter your name:")
age = eval(input("Enter your age:"))



#toddler 1 - 8
if age >= 1 and age <= 8 : 
	print("Toddler")

#preteen 9-14
elif age >= 9 and age <= 14 :
	print("Preteen")


#Teenager 15 - 18
elif age >= 15 and age <= 18:
	print("Teenager")

#Early Adulthood 19 - 27
elif age >= 19 and age <=27:
	print("Early Adulthood")


#Middle Age 28 - 44
elif age >= 28 and age <= 44:
	print("Middle Age")

#Past Adulthood 45 - 59
elif age >= 45 and age <= 59:
	print("Past Adulthood")


#Senior 60 - hanggang sa dulo ng ating walang hanggan.... jk 150
elif age >= 60 and age <=150:
	print("Senior")
else:
	print("Invalid")
	print("dinaig mo pa si enrile") 



	