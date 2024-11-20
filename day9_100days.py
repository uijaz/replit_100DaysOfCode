# Day 9 - Casting
print("== What generation are you a part of? ==")
year = int(input("What was your year of birth? "))
if year >= 1925 and year <= 1946:
  print("Traditionalists")
elif year >= 1947 and year <= 1964:
  print("Baby Boomers")
elif year >= 1965 and year <= 1981:
  print("Generation X")
elif year >= 1982 and year <= 1995:
  print("Millenials")
elif year >= 1996 and year <= 2015:
  print("Generation Z")
elif year >= 2016 and year <= 2023:
  print("Generation Alpha")
else:
  print("Too young or too old")
