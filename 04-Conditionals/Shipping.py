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

if len(sys.argv) != 2:
    print("Incorrect number of inputs! Please follow this format:")
    print("\tpython Shipping.py <package weight>")
else:
    weight = math.ceil(float(sys.argv[1]))
    cost = 0
    if weight < 0:
        print("The package cannot weigh less than 0 pounds.")
    elif weight > 100:
        print("The package weighs over 100 pounds and cannot be shipped.")
    else:
        costOverTwoPounds = 0 if (weight <= 2) else ((weight - 2) * 5)
        cost = 15 + costOverTwoPounds
        if weight > 70:
            cost += 15
        print(f"It will cost ${float(cost)} to ship your package.")
