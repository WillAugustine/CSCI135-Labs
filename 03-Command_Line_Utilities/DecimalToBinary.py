#########################################################################
#
# DecimalToBinary.py
#
# Author: Doug Galarus
#
# Description: Converts the first command line input from a decimal
#   into its binary number
#
# Command line inputs:
#   1 - Decimal number to be converted to binary (int)
#
# Example use:
#   python DecimalToBinary.py 10
#
#########################################################################

import sys

if len(sys.argv) != 2:
    print("Incorrect program use! Run program as follows:")
    print("\tpython DecimalToBinary.py <number to convert>")
else:
    print(bin(int(sys.argv[1]))[2:])