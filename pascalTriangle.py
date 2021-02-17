""" PASCAL'S TRIANGLE """
""" Builds and displays pascal's triangle. """
"""
To Do: Build the triangle to 'n' rows and display the result
"""
from os import system, name
#Clears Screen
def CLS():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

# Retrieves an integer from the user
# Returns the input
def INT(string):
    while True:
        try:
            userInput = int(input(string))
            return userInput
        except ValueError: CLS(), print("Please enter a number.")
numrows = INT("how many rows would you like?: ")
triangle = [ [ 1 for i in range(j+1) ] for j in range(numrows) ]
row = 2
while row < numrows:
    for term in range(len(triangle[row])-2):
        j = term + 1
        triangle[row][j] = triangle[row-1][j-1] + triangle[row-1][j]
    row += 1
print(triangle)
