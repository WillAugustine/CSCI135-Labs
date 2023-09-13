#########################################################################
#
# Lottery.py
#
# Author: Will Augustine
#
# Description: Use a nested if statement to determine if the inputted
#   numbers match the winning lottery numbers which are randomly generated
#
# Command line inputs:
#   1 - The first number of the lottery pick (int - between 1 and 10)
#   2 - The second number of the lottery pick (int - between 1 and 10)
#
# Example use:
#   python Lottery.py 7 3
#
#########################################################################

import sys
import random

if len(sys.argv) != 3:
    print("Incorrect number of inputs! Please follow this format:")
    print("\tpython Lottery.py <pick one> <pick two>")
else:
    pick1 = int(sys.argv[1])
    pick2 = int(sys.argv[2])
    if pick1 < 1 or pick1 > 10 or pick2 < 1 or pick2 > 10:
        print(f"ERROR: Your lottery picks ({pick1} & {pick2}) must both be in range 1-10.")
    else:
        winning1 = random.randint(1, 10)
        winning2 = random.randint(1, 10)
        print(f"The lottery numbers were {winning1} and {winning2}.")
        print(f"Your picks were {pick1} and {pick2}.")
        if (pick1 != winning1 and pick1 != winning2):
            if (pick2 != winning1 and pick2 != winning2):
                print("Sorry, no match.")
            else:
                print("You matched one number! You win $100!!")
        else:
            if (pick2 == winning1 or pick2 == winning2):
                print("You matched both numbers! Congratulations! You win $1000!!")
            else:
                print("You matched one number! You win $100!!")