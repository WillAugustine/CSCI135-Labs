#########################################################################
#
# Shipping.py
#
# Author: Will Augustine
#
# Description: Calculates the cost of shipping a package based on a series
#   of criteria regarding the package weight
#
# Command line inputs:
#   1 - The weight of the package in pounds (int)
#
# Example use:
#   python Shipping.py 75
#
#########################################################################

import sys
import math

# If incorrect use of file, let user know
if len(sys.argv) != 2:
    print("Incorrect number of inputs! Please follow this format:")
    print("\tpython Shipping.py <package weight>")
else:
    # Round weight up to next whole number
    weight = math.ceil(float(sys.argv[1]))
    # Start total cost at 0
    cost = 0
    # If the weight is less than 0, let the user know
    if weight < 0:
        print("The package cannot weigh less than 0 pounds.")
    # Otherwise, if the weight is over 100, package cannot be shipped
    elif weight > 100:
        print("The package weighs over 100 pounds and cannot be shipped.")
    # Otherwise (if package is valid weight)
    else:
        # Determine the cost over 2 pounds
        # If weight is less than 2 pounds, no additional cost is added
        costOverTwoPounds = 0 if (weight <= 2) else ((weight - 2) * 5)
        # Add additional cost over 2 pounds to cost for first 2 pounds
        cost = 15 + costOverTwoPounds
        # If weight is over 70, additional fee is added
        if weight > 70:
            cost += 15
        # Print total cost to ship package
        print(f"It will cost ${float(cost)} to ship your package.")
