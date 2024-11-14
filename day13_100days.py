# Day 13 - Gradebook Builder
print("== Grade Generator ==")

nameOfTest = input("What is the name of the test? ")
maxScore = int(input("What is the max score of this text? "))
pointsReceived = int(input("What was your score in this test? "))

percentage = round(pointsReceived / maxScore * 100, 2)  

if percentage >= 90 and percentage <= 100:
  print("You achieved A+ grade in your", nameOfTest, "test with", percentage, "% score.")
elif percentage >= 80 and percentage <= 89:
  print("You achieved A grade in your", nameOfTest, "test with", percentage, "% score.")
elif percentage >= 70 and percentage <= 79:
  print("You achieved B grade in your", nameOfTest, "test with", percentage, "% score.")
elif percentage >= 60 and percentage <= 69:
  print("You achieved C grade in your", nameOfTest, "test with", percentage, "% score.")
elif percentage >= 50 and percentage <= 59:
  print("You achieved D grade in your", nameOfTest, "test with", percentage, "% score.")
elif percentage < 50:
  print("You achieved U grade in your", nameOfTest, "test with", percentage, "% score.")
else:
  print("Invalid input.")
