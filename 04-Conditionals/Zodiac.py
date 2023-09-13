#########################################################################
#
# Zodiac.py
#
# Author: Will Augustine
#
# Description: Determines the Chinese zodiac sign given a year of birth
#
# Command line inputs:
#   1 - The year of birth to be converted to zodiac sign (int)
#
# Example use:
#   python Zodiac.py 2000
#
#########################################################################

import sys

if len(sys.argv) != 2:
    print("Incorrect number of inputs! Please follow this format:")
    print("\tpython Zodiac.py <birth year>")
else:
    birthYear = int(sys.argv[1])
    remainder = birthYear % 12
    zodiacSign = ""
    if remainder == 0:
        zodiacSign = "Monkey"
    if remainder == 1:
        zodiacSign = "Rooster"
    if remainder == 2:
        zodiacSign = "Dog"
    if remainder == 3:
        zodiacSign = "Pig"
    if remainder == 4:
        zodiacSign = "Rat"
    if remainder == 5:
        zodiacSign = "Ox"
    if remainder == 6:
        zodiacSign = "Tiger"
    if remainder == 7:
        zodiacSign = "Rabbit"
    if remainder == 8:
        zodiacSign = "Dragon"
    if remainder == 9:
        zodiacSign = "Snake"
    if remainder == 10:
        zodiacSign = "Horse"
    if remainder == 11:
        zodiacSign = "Sheep"

    print(f"You were born in the year of the {zodiacSign}.")