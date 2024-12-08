# Day 37 - String Slicing
print("== Star Wars Name Generator ==")
print()

while True:
  all_inputs = input("Enter your first name, last name, mother's maiden name, and where she came from, separated by spaces: ")
  fname, lname, m_name, m_city = all_inputs.split()
  sw_fname = fname[0:3].capitalize() + lname[0:3].lower()
  sw_lname = m_name[0:2].capitalize() + m_city[-3:].lower()
  print()
  print(f"Welcome to planet Naboo {sw_fname} {sw_lname}!")