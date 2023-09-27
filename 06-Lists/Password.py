#########################################################################
#
# Password.py
#
# Author: Will Augustine
#
# Description: With a hardcoded pin stored in an array, create a way to
#   prevent shoulder surfing by creating a list of random numbers to
#   map a numbers to, causing the password to be encoded
#
# Command line inputs: None
#
# Example use:
#   python Password.py
#
#########################################################################

import random

# Array for ordered numbers (0 - 9)
orderedNumbers = [x for x in range(10)]
# Array for random pin map (random number between 1 and 3)
randNumbers = [random.randint(1, 3) for x in range(10)]
# Create correct user password input array using random map from randNumbers array
mappedInput = [randNumbers[i] for i in range(5, 10)]
# Hardcoded correct pin from instructions
correctPin = [5, 6, 7, 8, 9]

# Print the pin and mapping key
pinKey = "PIN:"
numKey = "NUM:"
for i in range(len(orderedNumbers)):
    pinKey += f" {orderedNumbers[i]}"
    numKey += f" {randNumbers[i]}"
print(f"\n{pinKey}")
print(f"{numKey}\n")

# Get the user password attempt as a string
inputtedPin = input("Please enter your converted password: ")
# Convert the user password attempt to an array
guessedPin = [int(inputtedPin[i]) for i in range(len(inputtedPin))]

# If the password attempt is incorrect, let the user know
if (mappedInput != guessedPin):
    print("\nSorry, that password is incorrect.\n")
else:
    # Otherwise (the password attempt is correct), let the user know
    print("\nWelcome! You are correct.\n")