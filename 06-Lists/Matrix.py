#########################################################################
#
# Matrix.py
#
# Author: Will Augustine
#
# Description: Creates a 5x5 numeric matrix (initially all zeros) then
#   set all non-diagional values to 150*random.random() and print a
#   messy and a clean output
#
# Command line inputs: None
#
# Example use:
#   python Matrix.py
#
#########################################################################

import random

allZeros = [[0] * 5] * 5
messy = [[0] * 5] * 5

print("\nAll Zeros:")
for row in allZeros:
    rowString = ""
    for item in row:
        rowString += f"{item} "
    print(rowString)

print(f"len(messy): {len(messy)}")
print(f"len(messy[0]): {len(messy[0])}")
for rowNum in range(len(messy)):
    for colNum in range(len(messy[0])):
        if (rowNum != colNum):
            newNumber = 150 * random.random()
            print(f"newNumber: {newNumber}")
            print(f"at row {rowNum} and column {colNum}")
            messy[rowNum][colNum] = newNumber

print("\nMessy Output:")
for row in messy:
    rowString = ""
    for item in row:
        rowString += f"{item} "
    print(rowString)

# print("\nAll Zeros:")
# for row in allZeros:
#     rowString = ""
#     for item in row:
#         rowString += f"{item} "
#     print(rowString)