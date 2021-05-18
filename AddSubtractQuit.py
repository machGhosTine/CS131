# Assignment 8.3 - AddSubtractQuit.py
# This program will pass variables to different functions, and either perform a mathematical operation or quit based on user input
# Justin Middagh
# Hilbert College CS131
# October 24,2020

def main():
    # the following lines will establish the variables used throughout the rest of the program, to either pass to the other functions or quit the program
    first = int(input('Enter the first number: '))
    second = int(input('Enter the second number: '))
    choice = str(input('Do you wish to [A]dd, [S]ubtract, or [Q]uit? '))
    # the following lines are the if statements that determine what function will be called to pass the variables to, or quit altogether
    if choice == 'A' or choice == 'a':
        add(first, second)
    elif choice == 'S' or choice == 's':
        subtract(first, second)
    else:
        quit()


# the variables first/second will be added together as x/y, and printed to the screen
def add(x, y):
    addValue = x + y
    print(x, '+', y, '=', addValue)


# the variables first/second will be subtracted from one another as x/y, and printed to the screen
def subtract(x, y):
    subValue = x - y
    print(x, '-', y, '=', subValue)


main()
