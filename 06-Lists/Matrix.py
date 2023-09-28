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

# Creates a 5x5 array with all zeros
allZeros = [[0 for x in range(5)] for y in range(5)]
# Copies the all zero array to be used for updating values
messy = allZeros.copy()

# Prints all zero array using embedded for loop
print("\nAll Zeros:")
# For each row in the all zero array
for row in allZeros:
    # Create/reset variable to store row values
    rowString = ""
    # For each value in the current row
    for value in row:
        # Add value to all zero row string
        rowString += f"{value} "
    # Print the all zero row of values 
    print(rowString)

# Updates the messy array (currently all zeros) to have random floating-point
#   numbers everywhere besides the diagonals
#
# For each row index in messy array
for rowNum in range(len(messy)):
    # For each column index in messy row array
    for colNum in range(len(messy[0])):
        # If the position is NOT a diagional
        if (rowNum != colNum):
            # Update the value to random floating-point number
            messy[rowNum][colNum] = 150 * random.random()

# Prints the messy array using embedded for loop and while
#   storing values for clean output
print("\nMessy Output:")
# Create variable to store values for the clean output
cleanOutputString = ""
# For each row in the messy array
for row in messy:
    # Create/reset variable to store row values
    rowString = ""
    # For each value in the current row
    for value in row:
        # Add value to messy row string
        rowString += f"{value} "
        # Add rounded value with proper padding to clean output string
        cleanOutputString +=  f"{round(value, 2):>8.2f}"
    # Print the messy row of values 
    print(rowString)
    # Add newline character to clean output
    cleanOutputString += "\n"

# Prints the clean output string
print("\nClean Output:")
print(cleanOutputString)
