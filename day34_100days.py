# Day 34 - Pretty Printing
import os, time
os.system("clear")

def printEmail(email):
  print(f"Dear {email}\n",
        "It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.\n",
        "Love and hugs,",
        "Ian Spammington III",
        sep="\n")

def emailList():
  emails = ['user1@email.com', 'user2@email.com', 'user3@email.com', 'user4@email.com', 'user5@email.com', 'user6@email.com', 'user7@email.com', 'user8@email.com', 'user9@email.com', 'user10@email.com']
  return emails

print("Generating emails..")
time.sleep(1)
os.system("clear")

for email in emailList():
  printEmail(email)
  time.sleep(1)
  os.system("clear")
  time.sleep(1)
