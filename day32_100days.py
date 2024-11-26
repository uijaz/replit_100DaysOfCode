#Day 32 - Lists
import random

greetings = [
    "Hello",                # English
    "Bonjour",              # French
    "Hola",                 # Spanish
    "Zdravstvuyte",         # Russian
    "Nǐn hǎo",              # Chinese
    "Salve",                # Italian
    "Konnichiwa",           # Japanese
    "Guten Tag",            # German
    "Olá",                  # Portuguese
    "Anyoung haseyo",       # Korean
    "Asalaam alaikum",      # Arabic
    "Goddag",               # Danish
    "Shikamoo",             # Swahili
    "Goedendag",            # Dutch
    "Yassas",               # Greek
    "Dzień dobry",          # Polish
    "Selamat siang",        # Indonesian
    "Namaste",              # Hindi
    "God dag",              # Norwegian
    "Merhaba",              # Turkish
    "Shalom",               # Hebrew
    "God dag"               # Swedish
]

random_greeting = random.choice(greetings)
print(f"Hello to you in a different langauge: {random_greeting}!")