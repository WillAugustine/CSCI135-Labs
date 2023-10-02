#########################################################################
#
# ToPirate.py
#
# Author: Will Augustine
#
# Description: Given sentences inputted from the user, the known words
#   in a pirate translation dictionay will be switched to pirate words
#   and the translated sentence will be outputted. This is repeated
#   until the user inputs "quit" (not case sensitive)
#
# Command line inputs: None
#
# Example use:
#   python ToPirate.py
#
#########################################################################

# Dictionary to store english words as keys and pirate translation as value
pirateTranslator = {
    "hello": "avast",
    "excuse": "arrr",
    "sir": "matey",
    "boy": "matey",
    "man": "matey",
    "madam": "proud beauty",
    "officer": "foul blaggart",
    "the": "'th",
    "my": "me",
    "your": "yer",
    "is": "be",
    "are": "be",
    "restroom": "head",
    "restaurant": "galley",
    "hotel": "fleabag inn"
}

# Print the welcome message and instructions
print("Welcome to the English to Pirate translation service!")
print("\nWhen prompted, please enter a sentence in English and it will be translated \
to Pirate. Beware: the pirate translator’s vocabulary is limited, so try not \
to upset the pirate translator by using fancy words.")

# Get the english sentence from the user
# converts all characters to lowercase and splits them into an array
englishSentence = (input("\nPlease enter an English sentence:\n").lower()).split()

# While the user does not input "quit"
while englishSentence[0] != "quit":
    # Create/reset the pirate translation as a string
    pirateTranslation = ""
    # For each word in the inputted sentence
    for word in englishSentence:
        # If the word is in the pirateTranslator dictionary
        if word in pirateTranslator:
            # Add the translated word to the translation string
            pirateTranslation += pirateTranslator[word]
        else:
            # Add the current word to the translation string
            pirateTranslation += word
        # Add a space between words
        pirateTranslation += " "

    # Print the inputted sentence translated to pirate
    print("\nPirate Translation:")
    # capitalize() capitalizes the first word in the sentence
    print(pirateTranslation.capitalize())

    # Ask the user for another sentence to translate
    englishSentence = (input("\nPlease enter an English sentence:\n").lower()).split()

# Print message upon exit
print("\nThank ye, matey. Ahoy!\n\n")