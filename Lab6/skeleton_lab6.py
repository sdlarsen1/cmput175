import turtle

def fractal(myTurtle, depth, size):
	"""
	implement the recursive draw function
	"""
	if size > 20 and depth > 0:
		myTurtle.forward(size/3)
		myTurtle.left(60)
		fractal(myTurtle, depth-1, size-100)
		myTurtle.forward(size/3)
		fractal(myTurtle, depth-1, size-100)
		myTurtle.right(120)
		myTurtle.forward(size/3)
		fractal(myTurtle, depth-1, size-100)
		myTurtle.left(60)
		fractal(myTurtle, depth-1, size-100)

def main():
	myTurtle = turtle.Turtle()
	myScreen = turtle.Screen()
	
	myTurtle.color("green")
	fractal(myTurtle, 3, 300)
	myScreen.exitonclick()	

if __name__ == "__main__":
	main()
