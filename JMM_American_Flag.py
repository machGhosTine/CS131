#The Horrible American Flag
#This is a graphical representation of the American Flag using graphics.py
#Justin Middagh
#Hilbert College CS131
#October 3, 2020

from graphics import *


def horrible_American_flag():
#created window dimensions
    w = 96
    h = 182.4
#created graphwin named flag, set all values for red rectangle
    win = GraphWin("Flag", w, h)
    uleft = Point(0, 0)
    lright = Point(300, 150)
    rect1 = Rectangle(uleft, lright)
    rect1.setFill(color_rgb(178, 34, 52))
    rect1.setWidth(0)
    rect1.draw(win)
#created/set all values for the blue rectangle
    uleft1 = Point(0,0)
    lright1 = Point(55,55)
    rect2 = Rectangle(uleft1,lright1)
    rect2.setFill(color_rgb(60, 59, 110))
    rect2.setWidth(0)
    rect2.draw(win)
#created all the lines, set values for each
    line1 = Line(Point(10,55), Point(10,150))
    line1.setFill(color_rgb(255, 255, 255))
    line1.setWidth(8)
    line1.draw(win)
    line1 = Line(Point(25,55), Point(25,150))
    line1.setFill(color_rgb(255, 255, 255))
    line1.setWidth(8)
    line1.draw(win)
    line1 = Line(Point(40,55), Point(40,150))
    line1.setFill(color_rgb(255, 255, 255))
    line1.setWidth(8)
    line1.draw(win)
    line1 = Line(Point(55,0), Point(55,150))
    line1.setFill(color_rgb(255, 255, 255))
    line1.setWidth(8)
    line1.draw(win)
    line1 = Line(Point(70,0), Point(70,150))
    line1.setFill(color_rgb(255, 255, 255))
    line1.setWidth(8)
    line1.draw(win)
    line1 = Line(Point(85,0), Point(85,150))
    line1.setFill(color_rgb(255, 255, 255))
    line1.setWidth(8)
    line1.draw(win)
    
    win.getMouse() 
    win.close()
    

horrible_American_flag()

