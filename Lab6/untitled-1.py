import turtle

def fractal(myTurtle, depth, size):
	"""
	implement the recursive draw function
	-don't have to change the size each call
	"""
	if depth == 0:
		myTurtle.forward(size)
	else:
		fractal(myTurtle, depth-1, size)
		myTurtle.left(60)
		fractal(myTurtle, depth-1, size)
		myTurtle.right(120)
		fractal(myTurtle, depth-1, size)
		myTurtle.left(60)
		fractal(myTurtle, depth-1, size)

def main():
	myTurtle = turtle.Turtle()
	myScreen = turtle.Screen()
	
	myTurtle.color("purple")
	fractal(myTurtle, 3, 25)
	myScreen.exitonclick()	

if __name__ == "__main__":
	main()