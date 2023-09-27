#########################################################################
#
# PickTeams.py
#
# Author: Will Augustine
#
# Description: The user will enter a team name as well as players on
#   the team (one by one via the input method NOT command line input)
#   and the team information will be displayed
#
# Command line inputs: None
#
# Example use:
#   python PickTeams.py
#
#########################################################################

# Prints information about the program
print("----------------------------------------------------------------------------")
print("This program collects information about teams including team names and player names.")
print("It creates and displays a report of teams and players at the end.")
print("----------------------------------------------------------------------------\n\n")

# Gather the number of teams from the user input
numOfTeams = int(input("How many teams are there? "))

# If number of teams is not in appropriate range, let user know
if (numOfTeams < 2 or numOfTeams > 10):
    print("\nThe number of teams should be between 2 and 10!")
else:
    # Add instructions for inputting player names for each team to final message
    outputMessage = "\nPlease enter a team name when prompted. Then enter player names for that team."
    outputMessage += "\nWhen done entering player names for that team, type done.\n"

    # Loop for number of teams user inputted
    for i in range(1, numOfTeams + 1):
        print()
        # Gather the currenet team name from the user
        teamName = input(f"Please enter the name of Team #{i}: ")
        # Gather the first player name from the user
        playerName = input(f"Please enter the name of a player for team {teamName}: ")

        outputMessage += "\n\n------------------------------"
        outputMessage += f"\nTeam #{i}: {teamName}"
        outputMessage += "\n------------------------------"

        playerNumber = 1
        # While the player did not input "done" (not case sensitive) for player name
        while(playerName.lower() != "done"):
            # Add player name to playerNames array
            outputMessage += f"\nPlayer #{playerNumber}: {playerName}"
            playerNumber += 1
            # Get the next player name from the user
            playerName = input(f"Please enter the name of a player for team {teamName}: ")
        
        outputMessage += "\n------------------------------"

    print(outputMessage)