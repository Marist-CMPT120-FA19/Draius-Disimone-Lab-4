#traffic light draius disimone 
from graphics import*

def main():
#open new window to do 
	win= GraphWin()
	#define shape
	shape= Rectangle(Point(2,20), Point(40,100))
	shape.setOutline("black")
	shape.draw(win)
	shape.setFill("black")
	#red light
	red=Circle(Point(20,40),8)
	red.setOutline("black")
	red.draw(win)
	red.setFill("red")
	#yellow light
	yellow=Circle(Point(20,60), 8)
	yellow.setOutline("black")
	yellow.setFill("yellow")
	yellow.draw(win)
	#green light
	green=Circle(Point(20,80),8)
	green.setOutline("black")
	green.setFill("green")
	green.draw(win)
	#click to close window
	win.getMouse()
	win.close()
main()
