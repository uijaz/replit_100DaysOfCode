# Day 41 - Dictionaries with Loops
import os
os.system('clear')

web_dict = {}
print("🌟Website Rating🌟")

name = input("Input the website name: ")
web_dict.update({"name":name})

url = input("Input the URL: ")
web_dict.update({"url":url})

desc = input("Input your a description: ")
web_dict.update({"desc":desc})

rating = input("Input the a star(*) rating out of 5: ")
web_dict.update({"rating":rating})

print()
dict_index = 0
for name, value in web_dict.items():
    dict_index += 1
    if dict_index < len(web_dict):
      print(f"{name}:{value}", end=", ")
    else:
         print(f"{name}:{value}")