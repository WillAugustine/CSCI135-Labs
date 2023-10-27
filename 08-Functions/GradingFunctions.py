#########################################################################
#
# GradingFunctions.py
#
# Author: Will Augustine
#
# Description: A collection of functions to determine grades based on
#   hard coded cutoff values and their corresponding letter grades
#
# Command line inputs: None
#
# Example use:
#   python GradingFunctions.py
#
#########################################################################

# Numerical cutoff values for letter grades
cutoffs = [100, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 0]
# Letter grades corresponding to numerical cutoff values
letterGrades = ['A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']

#
# Prints the grading scale to standard output using print()
#
# Inputs: None
#
# Outputs: None
#
def printGradingScale():
    # Grading scale header, seperatd by tab (\t)
    print("Percent Range\tLetter Grade")
    print("-------------\t-------------")

    # Starting at 0, loop until length of letterGrades array is reached
    for i in range(len(letterGrades)):

        # If on the last letter grade
        if (i == len(letterGrades ) - 1):
            print(f"Below {cutoffs[i]}%\t{letterGrades[i]}")

        # Otherwise, if on the first letter grade
        elif (i == 0):
            print(f"{cutoffs[i+1]} to {cutoffs[i]}%\t{letterGrades[i]}")

        # Otherwise, print using regular formatting
        else:
            print(f"{cutoffs[i+1]} to <{cutoffs[i]}%\t{letterGrades[i]}")
    
#
# Returns the letter grade corresponding to the score.
#   For example, 'A-' is returned for a score of 0.9
#
# Inputs:
#   score: a float value between 0.0 and 1.0 (inclusive), representing percentage
#       For example, 0.9 represents 90%
#
# Outputs: A string containing a letter grade
#
def getGradeByScore(score):
    # Starting at 0, loop until length of letterGrades array minus 1 is reached
    for i in range(len(cutoffs) - 1):
        # Set the upper limit cutoff value - divide by 100 to get float value
        upperLimit = cutoffs[i]/100
        # Set the lower limit cutoff value - divide by 100 to get float value
        lowerLimit = cutoffs[i+1]/100
        # If score is between score and upper/lower limits
        if ((score < upperLimit) and (score >= lowerLimit)):
            # Return corresponding letter grade
            return letterGrades[i]
    return letterGrades[0]

def getGradeByScores(scores):
    totalScore = 0
    for score in scores:
        totalScore += score
    averageScore = totalScore / len(scores)
    return getGradeByScore(averageScore)

def getGradeByPoints(pointsEarned, pointsPossible):
    totalPointsEarned = 0
    for score in pointsEarned:
        totalPointsEarned += score

    totalPointsPossible = 0
    for score in pointsPossible:
        totalPointsPossible += score
    
    return getGradeByScore(totalPointsEarned / totalPointsPossible)

def getGradeRange(strGrade):
    for i in range(len(letterGrades)):
        if letterGrades[i] == strGrade:
            return (cutoffs[i+1], cutoffs[i])

if __name__ == "__main__":
    printGradingScale()

    strGrade = getGradeByScore(.75)
    print(f"grade for 90%: {strGrade}")

    scores = [0.95, 0.8, 0.85]
    strGrade = getGradeByScores(scores)
    print(f"average grade for {scores} is {strGrade}")

    pointsEarned = [8, 9, 15]
    pointsPossible = [10, 10, 20]
    strGrade = getGradeByPoints(pointsEarned, pointsPossible)
    print(f"grade for points earned {pointsEarned} and points possible {pointsPossible} is {strGrade}")

    grade = 'B+'
    tupleGradeRange = getGradeRange(grade)
    print(f'grade range for {grade} is {tupleGradeRange}')