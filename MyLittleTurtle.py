import turtle
Tuples = ((0, 0), (0.0, 40.0), (40.0, 40.0), (40.0, 40.0), (40.0, 40.0), (40.0, 40.0))
turtle.mode("logo")
turtle.begin_poly()
for i in Tuples:
    turtle.goto(i)
turtle.end_poly()
p = turtle.get_poly()
turtle.register_shape("myFavouriteShape", p)
turtle.shape("myFavouriteShape")
turtle.goto(0, 0)
turtle.clear()
turtle.mainloop()