#Inches to meters GUI
#this program takes the conversion of inches to meters into a rudimentary graphical user interface
#Justin Middagh
#Hilbert College CS131
#October 4,2020

from graphics import *

def inches2meters():
#title of my window and main title up top
    win = GraphWin("Inch2Meter", 500, 500)
    txt = Text(Point(250,10), "Inches to Meters Converter").draw(win)
    txt.setSize(15)
#inches to meters input box with text below    
    input_box = Entry(Point(250,200), 4)
    Text(Point(250,230), "Inches to be Converted").draw(win)
    input_box.setText("")
    input_box.draw(win)
#this is where the conversion will display (location)  
    output_box = Text(Point(250,300.5),"")
    output_box.draw(win)
#the convert button   
    button = Text(Point(250,450),"Click here to convert!")
    button.draw(win)
#this will wait for the user input
    win.getMouse()
#mathematical conversion
    inches = float(input_box.getText())
    meters = inches * 2.54
#this will display the conversion along with text
    output_box.setText(round(meters,2))
    Text(Point(250,320), " Meters!").draw(win)
# wait for the click, then quit
    win.getMouse()
    win.close()
    
inches2meters()











