import tkinter
from turtle import Turtle, Screen



screen = Screen()
screen.setup(1000,700)
screen.title("Shape Drawing Program")
screen.colormode(1)

turtle = Turtle()


turtle.speed(10000)

#Number of sides, the size, and the selected option. (n,s,o)
def drawShape(n,s,o):
	sexta = (n-2)*180
	exta = (sexta/n)
	inta = 180-(exta)

##This draws the shape by edges.
	if o == 1:
		for i in range(n):
			turtle.forward(inta*s)
			turtle.left(inta)
#This draws the shape by points instead.
	elif o == 2:
		for i in range(n):
			turtle.left(exta*2)
			turtle.forward(exta*s)
##If you didn't enter a valid option, this puts out to the console
#That you error'ed out.
	else:
		print("You bumbling fool. You raging idiot.")


#51.4
#Define the number of sides, the size, and the way the shape is drawn.
def drawCirclefromShape(n,s,o):
	stage = 1
	inc = .03
	r = 1
	g = 0
	b = 0

	for i in range(360):
		stage = i // 30
		if stage == 2:
			g += inc
		if stage == 4:
			r -= inc
		if stage == 6:
			b += inc
		if stage == 8:
			g -= inc
		if stage == 10:
			r += inc
		if stage == 12:
			b -= inc
			
		turtle.pencolor(r,g,b)
		drawShape(n,s,o)
		turtle.right(1)


drawCirclefromShape(8,3,1)
screen.mainloop()
