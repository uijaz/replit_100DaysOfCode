# Day 6 - Elif
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "john" and password == "pass":
  print("Welcome John!")
elif username == "jane" and password == "word":
  print("Hey there Jane!")
elif username == "root" and password == "pwd":
  print("You now have root access.")
else:
  print("Access denied!")
