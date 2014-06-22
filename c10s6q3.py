import turtle           # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()

# Position tess onto the place where the green light should be
red=turtle.Turtle()
yellow=turtle.Turtle()
red.penup()
yellow.penup()
tess.forward(40)
tess.left(90)
tess.forward(40)
tess.shape("circle")
tess.shapesize(2)
tess.color("green")

red.forward(40)
red.left(90)
red.forward(120)
red.shape("circle")
red.shapesize(2)
red.color("red")


yellow.forward(40)
yellow.left(90)
yellow.forward(80)
yellow.shape("circle")
yellow.shapesize(2)
yellow.color("yellow")

red.hideturtle()
yellow.hideturtle()


stateNumber=0#FUCK UNDERSCORES, CAMEL CASE FTW
def stateThingy():
	global stateNumber
	if stateNumber==0:
		yellow.showturtle()
		tess.hideturtle()
		stateNumber=1
	elif stateNumber==1:
		ye llow.hideturtle()
		red.showturtle()
		stateNumber=2
	else:
		red.hideturtle()
		tess.showturtle()
		stateNumber=0
		pass
wn.onkey(stateThingy,"space")
wn.listen()
wn.mainloop()

#I prefer the method given in the lesson. the above method opens up the possibilty of 2 traffic lights being on at the same time, that doesn't happen in real