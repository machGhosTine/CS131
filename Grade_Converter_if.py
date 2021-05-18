# Assignment 9.3 - Grade_Converter.py
# This program will accept an integer exam score as input, and based on a decision structure consisting of if statements, output the corrosponding letter grade
# Justin Middagh
# Hilbert College CS131
# November 1,2020

def Grade_Converter():
    # the int value input is taken for use throughout the if statement block
    grade = int(input("Please enter your numerical grade score to be converted to a letter grade: "))
    # the block of if statements serve as a decision structure to convert the int value to a letter grade, and will print the conversion to the screen
    if grade >= 90:
        print('Your grade of', grade, 'is an A')
    elif grade >= 80:
        print('Your grade of', grade, 'is a B')
    elif grade >= 70:
        print('Your grade of', grade, 'is a C')
    elif grade >= 60:
        print('Your grade of', grade, 'is a D')
    else:
        print('Your grade of', grade, 'is an F')


Grade_Converter()
