#########################################################################
#
# BinaryToDecimal.py
#
# Author: Will Augustine
#
# Description: Converts a binary number inputted on the command line
#   into its integer representation
#
# Command line inputs:
#   1 - The binary number to be converted into an integer (bin)
#
# Example use:
#   python BinaryToDecimal.py 1010
#
#########################################################################

import sys

if len(sys.argv) != 2:
    print("Incorrect program use! Run program as follows:")
    print("\tpython BinaryToDecimal.py <number to convert>")
else:
    print(int(sys.argv[1], 2))