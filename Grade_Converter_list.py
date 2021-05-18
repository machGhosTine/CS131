#Assignment 9.3 - Grade_Converter.py
#This program will accept an integer exam score as input, and through the the creation of a list and an index, will output the corrosponding letter grade
#Justin Middagh
#Hilbert College CS131
#November 1,2020

def Grade_Converter():
    grade = int(input("Please enter your numerical grade to be converted to a letter grade: "))
    index = int(grade)/10
    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]
    final = grades[int(index)]
    print('Your numerical grade of',grade,'converts to a letter grade of:',final)

Grade_Converter()