import turtle
screen = turtle.Screen()
Tuples = ((-118.0, 5.0), (-88.0, 73.0), (-76.0, 32.0), (-93.0, 28.0), (-85.0, 17.0))
MyVeryOwnShape_turtle = turtle.Turtle()
turtle.colormode(255)
turtle.mode("logo")
screen.register_shape("MyVeryOwnShape", Tuples)
MyVeryOwnShape_turtle.shape("MyVeryOwnShape")
turtle.mainloop()