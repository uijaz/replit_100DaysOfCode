#myGPTexperiment
# using Copilot with GPT-4o
# Day 65: Character Creation

# Specs:
# - This is a game that will have characters, enemies and players.
# - This game needs to have a 'character' class with attributes of 'name', h'ealth' and 'magic points'.
# - This class needs these values setup when it is initialized.
# - It then needs a method to output this data.
# - There is a sub-class 'player' which inherits from 'character' and also has an attribute of 'number of lives'.
# - Player should also have an 'am I alive?' method which checks the player status and reports back yes or no.
# - There is also an 'enemy' sub-class with additional attributes of 'type' and 'strength'.
# - 'enemy' should have two sub-classes:
# -- 'orc' with a 'speed' attribute.
# -- 'vampire' with a 'day/night' tracker.
# - Instantiate the game and ask the user to name one player, two vampires and three orcs.
# - Print out their values.

# Example output:
# 🌟Generic RPG🌟
# 
# 🚩Enter names for the following characters:
# Your name > David
# Vampire name > Boris
# Vampire name > Rishi
# Orc name > Bill
# Orc name > Ted
# Orc name > Station
# 
# 🚩Character values are as follows:
# Name: David
# Health: 100
# Magic Points: 50
# Lives: 3
# Alive?: Yes
# 
# Name: Boris
# Health: 45
# Magic Points: 70
# Type: Vampire
# Strength: 3
# Day/Night?: Night
# 
# Name: Rishi
# Health: 70
# Magic Points: 10
# Type: Vampire
# Strength: 75
# Day/Night?: Day
# 
# Name: Bill
# Health: 60
# Magic Points: 5
# Type: Orc
# Strength: 75
# Speed: 90
# 
# Name: Ted
# Health: 75
# Magic Points:40
# Type: Orc
# Strength: 80
# Speed: 45
# 
# Name: Station
# Health: 35
# Magic Points: 40
# Type: Orc
# Strength: 49
# Speed: 50

class Character:
  name = None
  health = None
  magic_points = None

  def __init__(self, name, health, magic_points):
    self.name = name
    self.health = health
    self.magic_points = magic_points

  def display(self):
    return f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}\n"


class Player(Character):
  def __init__(self, name, health, magic_points, lives):
    super().__init__(name, health, magic_points)
    self.lives = lives

  def is_alive(self):
    return self.lives > 0

  def display(self):
    alive_status = "Yes" if self.is_alive() else "No"
    return super().display() + f"Lives: {self.lives}\nAlive?: {alive_status}\n"


class Enemy(Character):
  def __init__(self, name, health, magic_points, enemy_type, strength):
    super().__init__(name, health, magic_points)
    self.enemy_type = enemy_type
    self.strength = strength

  def display(self):
    return super().display() + f"Type: {self.enemy_type}\nStrength: {self.strength}\n"


class Orc(Enemy):
  def __init__(self, name, health, magic_points, strength, speed):
    super().__init__(name, health, magic_points, "Orc", strength)
    self.speed = speed

  def display(self):
    return super().display() + f"Speed: {self.speed}\n"


class Vampire(Enemy):
  def __init__(self, name, health, magic_points, strength, day_night):
    super().__init__(name, health, magic_points, "Vampire", strength)
    self.day_night = day_night

  def display(self):
    return super().display() + f"Day/Night?: {self.day_night}\n"


def main():
  print("🌟Generic RPG🌟\n")
  print("🚩Enter names for the following characters:")

  player_name = input("Your name > ")
  player = Player(player_name, 100, 50, 3)

  vampires = []
  for i in range(2):
    vampire_name = input(f"Vampire name > ")
    vampires.append(Vampire(vampire_name, 45 + i * 25, 70 - i * 60, 3 + i * 72, "Night" if i == 0 else "Day"))

  orcs = []
  for i in range(3):
    orc_name = input(f"Orc name > ")
    orcs.append(Orc(orc_name, 60 + i * 15, 5 + i * 35, 75 + i * 5, 90 - i * 45))

  print("\n🚩Character values are as follows:")
  print(player.display())
  for vampire in vampires:
    print(vampire.display())
  for orc in orcs:
    print(orc.display())


if __name__ == "__main__":
  main()