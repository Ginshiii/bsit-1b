prelim = eval(input("Input your prelim grade --> "))
midterm = eval(input("Input your midterm grade --> ")) 
semifinal = eval(input("Input your semi final grade --> "))
final = eval(input("Input your final grade --> "))
quiz = eval(input("Input your quiz grade --> "))
project = eval(input("Input your project grade --> "))

FG = (prelim* 0.15) + (midterm* 0.15) + (semifinal* 0.15) + (final* 0.15) + (quiz* 0.25) + (project* 0.15)

if FG >= 75:

	print("Congratulations! You passed the course")

else: 
	print("Sorry You Failed")
	print("Yan tamad mo kasi... bawi ka nalang next life")