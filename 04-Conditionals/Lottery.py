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

# If program is used incorrectly, let the user know
if len(sys.argv) != 3:
    print("Incorrect number of inputs! Please follow this format:")
    print("\tpython Lottery.py <pick one> <pick two>")
else:
    # Get user picks from command line arguments
    pick1 = int(sys.argv[1])
    pick2 = int(sys.argv[2])
    # If picks are not valid (not between 1 and 10), let the user know
    if pick1 < 1 or pick1 > 10 or pick2 < 1 or pick2 > 10:
        print(f"ERROR: Your lottery picks ({pick1} & {pick2}) must both be in range 1-10.")
    # Otherwise (if picks are valid)
    else:
        # Randomly get winning numbers
        winning1 = random.randint(1, 10)
        winning2 = random.randint(1, 10)

        # Print user picked numbers and winning numbers
        print(f"The lottery numbers were {winning1} and {winning2}.")
        print(f"Your picks were {pick1} and {pick2}.")

        # Test for all 4 single match combinations. If one pick matches, check if the other
        #   user pick matches the other winning pick. Display if the user matched one
        #   or both picks, and how much they won
        if (pick1 == winning1):
            if (pick2 == winning2):
                print("You matched both numbers! Congratulations! You win $1000!!")
            else:
                print("You matched one number! You win $100!!")
        elif (pick1 == winning2):
            if (pick2 == winning1):
                print("You matched both numbers! Congratulations! You win $1000!!")
            else:
                print("You matched one number! You win $100!!")
        elif (pick2 == winning1):
            if (pick1 == winning2):
                print("You matched both numbers! Congratulations! You win $1000!!")
            else:
                print("You matched one number! You win $100!!")
        elif (pick2 == winning2):
            if (pick1 == winning1):
                print("You matched both numbers! Congratulations! You win $1000!!")
            else:
                print("You matched one number! You win $100!!")
        # Otherwise (if no picks matched)
        else:
            # Display that the user did not have any matches
            print("Sorry, no match.")