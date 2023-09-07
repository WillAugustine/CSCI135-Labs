#########################################################################
#
# HexToDecimal.py
#
# Author: Will Augustine
#
# Description: Convertes the inputted hex value into its decimal
#   representation (not case sensitve)
#
# Command line inputs:
#   1 - Number of flights in building (int)
#
# Example use:
#   python HexToDecimal.py 7e4
#
#########################################################################

import sys

if len(sys.argv) != 2:
    print("Incorrect program use! Run program as follows:")
    print("\tpython HexToDecimal.py <number to convert>")
else:
    print(int(sys.argv[1], 16))