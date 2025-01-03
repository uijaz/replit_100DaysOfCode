#myGPTexperiment
# using Copilot with GPT-4o
# Day 64: OOP

# Specs:
# - Create a generic 'job' class.
# - The init method of 'job' will store the details for name, salary and hours worked.
# - 'job' will have another method that prints those details nicely.
# - Create two sub-classes from 'job': 'doctor' and 'teacher'
# - The 'doctor' subclass should include 'speciality' and 'years of experience' methods.
# - The 'teacher' subclass should include 'subject' and 'position'.
# - The print methods for each sub-class should print this extra data.
# - Instantiate a lawyer, a computer science teacher, and a pediatric doctor with 7 years of experience.
# - Output the information for each job.

# Example output:
# 🌟Jobs Jobs Jobs!🌟
# 
# Job type: Lawyer
# Salary: $ Squillions
# Hours worked: 60
# 
# Job type: Teacher
# Salary: $ Nowhere near enough
# Hours worked: All of them
# Subject: Computer Science
# Position: Classroom Teacher
# 
# Job type: Doctor
# Salary: $ Doing very nicely thank you
# Hours worked: 50
# Speciality: Pediatric Consultant
# Years of Experience: 7

class Job:
  name = None
  salary = None
  hours_worked = None

  def __init__(self, name, salary, hours_worked):
    self.name = name
    self.salary = salary
    self.hours_worked = hours_worked

  def print_details(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours_worked}")

class Doctor(Job):
  def __init__(self, name, salary, hours_worked, speciality, years_experience):
    super().__init__(name, salary, hours_worked)
    self.speciality = speciality
    self.years_experience = years_experience

  def print_details(self):
    super().print_details()
    print(f"Speciality: {self.speciality}")
    print(f"Years of Experience: {self.years_experience}")

class Teacher(Job):
  def __init__(self, name, salary, hours_worked, subject, position):
    super().__init__(name, salary, hours_worked)
    self.subject = subject
    self.position = position

  def print_details(self):
    super().print_details()
    print(f"Subject: {self.subject}")
    print(f"Position: {self.position}")

print("🌟Jobs Jobs Jobs!🌟")
print()

lawyer = Job("Lawyer", "$ Squillions", 60)
teacher = Teacher("Teacher", "$ Nowhere near enough", "All of them", "Computer Science", "Classroom Teacher")
doctor = Doctor("Doctor", "$ Doing very nicely thank you", 50, "Pediatric Consultant", 7)

lawyer.print_details()
print()
teacher.print_details()
print()
doctor.print_details()
print()