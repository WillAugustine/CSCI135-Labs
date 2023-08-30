#########################################################################
#
# HelloArgs.py
#
# Author: Will Augustine
#
# Description: Takes four command line arguments to display a message
#
# Command line inputs:
#   1 - A general greeting word (Hello, Greetings, etc.)
#   2 - The name of someone
#   3 - The name of someone
#   4 - The name of someone
#
#########################################################################

import sys

def main():
    if len(sys.argv) != 5:
        print("Invalid inputs! Please follow the format:")
        print("\tpython HelloArgs.py [Greeting] [Name #1] [Name #2] [Name #3]")

    else:
        greeting = sys.argv[1]
        names = sys.argv[2:]
        for name in names:
            print(f"{greeting} {name}!")

if __name__ == "__main__":
    main()    