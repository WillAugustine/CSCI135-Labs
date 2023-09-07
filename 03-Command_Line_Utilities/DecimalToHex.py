#########################################################################
#
# DecimalToHex.py
#
# Author: Will Augustine
#
# Description: Converts the inputted decimal value to its hex representation
#
# Command line inputs:
#   1 - Decimal number to be converted to hex (int)
#
# Example use:
#   python DecimalToHex.py 2020
#
#########################################################################

import sys

if len(sys.argv) != 2:
    print("Incorrect program use! Run program as follows:")
    print("\tpython DecimalToHex.py <number to convert>")
else:
    print(hex(int(sys.argv[1]))[2:])