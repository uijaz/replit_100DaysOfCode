#myGPTexperiment
# using Copilot with GPT-4o
# Day 60: The Magic of Time

# Specs:
# Austomatically work out today's date.
# Prompt the user to input the name and date of their event (year, month and day).
# Work out the number of days until the event and output it, insert relevant emojis.
# If the event is happening today, insert some party emojis.
# If the event was in the past, sad face emojis and tell the user how many days ago it was.

# Example output:
# 🌟Event Countdown Timer🌟
# 
# Input the event > Nan's 100th birthday
# Input the year > 2022
# Input the month > 10
# Input the day > 16
# 
# 🎉🎉Nan's 100th birthday is today! 🎉🎉

from datetime import datetime

# Get today's date
today = datetime.today().date()

# Prompt the user to input the event details
event_name = input("Input the event > ")
event_year = int(input("Input the year > "))
event_month = int(input("Input the month > "))
event_day = int(input("Input the day > "))

# Create a datetime object for the event
event_date = datetime(event_year, event_month, event_day).date()

# Calculate the difference between the event date and today
delta = event_date - today

# Output the result with relevant emojis
print("\n🌟Event Countdown Timer🌟\n")
if delta.days > 0:
  print(f"⏳ {event_name} is in {delta.days} days! ⏳")
elif delta.days == 0:
  print(f"🎉🎉 {event_name} is today! 🎉🎉")
else:
  print(f"😢 {event_name} was {-delta.days} days ago. 😢")