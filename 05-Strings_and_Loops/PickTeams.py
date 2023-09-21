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
    print("\nERROR: The number of teams should be between 2 and 10 (inclusive)!")
else:
    # Print instructions for inputting player names for each team
    print("\nPlease enter a team name when prompted. Then enter player names for that team.")
    print("When done entering player names for that team, type done.\n")

    # Create empty dictionary for storing team info
    #   key: team name
    #   value: array of player names
    teamInfo = {}

    # Loop for number of teams user inputted
    for i in range(numOfTeams):
        print()
        # Gather the currenet team name from the user
        teamName = input(f"Please enter the name of Team #{i + 1}: ")
        # Gather the first player name from the user
        playerName = input(f"Please enter the name of a player for team {teamName}: ")
        # Create empty array to store player names (will be used in teamInfo dictionary)
        playerNames = []

        # While the player did not input "done" (not case sensitive) for player name
        while(playerName.lower() != "done"):
            # Add player name to playerNames array
            playerNames.append(playerName)
            # Get the next player name from the user
            playerName = input(f"Please enter the name of a player for team {teamName}: ")
        
        # Add entry in teamInfo dictionary
        teamInfo[teamName] = playerNames

    # Counter for team being displayed
    teamNumber = 1

    # For each key value pair in the teamInfo dictionary
    for teamName, playerNames in teamInfo.items():
        # Print team number and name
        print("\n------------------------------")
        print(f"Team #{teamNumber}: {teamName}")
        print("------------------------------")

        # Counter for player being displayed
        playerNumber = 1

        # Iterate playerNames array, setting current item to player variable
        for player in playerNames:
            # Print player information
            print(f"Player #{playerNumber}: {player}")
            # Increment playerNumber counter
            playerNumber += 1

        # Increment teamNumber counter
        teamNumber += 1

        print("------------------------------")