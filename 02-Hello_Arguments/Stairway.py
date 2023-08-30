#########################################################################
#
# Stairway.py
#
# Author: Will Augustine
#
# Description: Calculates total number of steps in building stairway
#   and the total vertical height of stairway
#
# Command line inputs:
#   1 - Number of flights in building (int)
#   2 - Number of steps per flight (int)
#   3 - Height of a step in feet (float)
#
#########################################################################

import sys

def main():
    if len(sys.argv) != 4:
        print("Invalid inputs! Please follow the format:")
        print("\tpython Stairway.py [# of flights] [# of steps per flight] [height of a step in feet]")

    else:
        flights = int(sys.argv[1])
        stepsPerFlight = int(sys.argv[2])
        stepHeight = float(sys.argv[3])
        print(f"Total steps: {flights * stepsPerFlight}")
        print(f"Total height in feet: {flights * stepsPerFlight * stepHeight}")

if __name__ == "__main__":
    main()    