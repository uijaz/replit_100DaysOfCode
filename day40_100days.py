# Day 40 - Dictionaries
import os
os.system('clear')

print("🌟Contact Card🌟")
user_dict = {}

name = input("Input your name > ")
user_dict.update({"name":name})

dob = input("Input your date of birth (dd/mm/yyyy) > ")
user_dict.update({"dob":dob})

tel = input("Input your telephone number > ")
user_dict.update({"tel":tel})

email = input("Input your email > ")
user_dict.update({"email":email})

address = input("Input your address > ")
user_dict.update({"address":address})
print()
print(f"""Hi {user_dict.get('name')}. Our dictionary says that you were born on {user_dict.get('dob')}, we can call you on {user_dict.get('tel')}, email {user_dict.get('email')}, or write to {user_dict.get('address')}.""")