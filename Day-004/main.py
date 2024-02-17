# User Input
name = input("What is your name?")
enemy = input("What is your worst enemy’s name?")
power = input("What is your superpower?")
location = input("Where do you live?")
food = input("What is your favorite food?")

# Welcome message
print(f"Hello {name}! Your ability to {power} will make sure you never have to look at {enemy} again")
print(f"Go eat {food} as you walk down the streets of {location} and use {power} for good")

# Introduction
print(f"Go grab some {food} as you walk down the streets of {location}.")
print(f"A villainous plot unfolds before you. Will you use {power} for good or succumb to evil?")

# User choice
choice = input("Do you want to fight for good or succumb to evil? (g/e)")

if choice == "g":
  print(f"{name}, armed with your {power} and fueled by {food}, you stand before the villainous plot. Will you use your {power} for good")
elif choice == "e":
  print(f"{name}, armed with your {power} and fueled by {food}, you stand before the villainous plot. Will you use your {power} for evil")
else:
  print(f"Indecision clouds your judgement. You must make a choice. Will you use your {power} for good or succumb to...")

# Ending message
print(f"Your adventure ends here. Thank you for playing {name}.")

