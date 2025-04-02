# this imports the libraries used by this code and what they need from it
import turtle as t
import tkinter as tk
from turtle import Turtle
from turtle import Screen
from tkinter import ttk

class Controller:
    def __init__(self, turtle_name):
        self.turtle = turtle_name

    def main_loop(self):
        guidelines = ("Here are the controls for the program:\n"
                      "'WASD' is used for movement\n"
                      "you can use 'Q' to make a tuple for your turtle shape.\n"
                      "'R' is to undo the last action you have done\n"
                      "Once you have a shape you can press 'ENTER' to get your file\n"
                      "And you can close your program by pressing 'C'\n")
        print(guidelines)
        screen.onkeyrelease(self.turtle.save_tuple, "q")
        screen.onkeyrelease(self.turtle.tuple_of_tuples, "Return")
        screen.onkeyrelease(quit, "c")
        screen.onkeyrelease(self.turtle.home, "h")
        screen.onkeypress(self.turtle.undo_last, "r")
        screen.onkeypress(self.turtle.move_up,"w")
        screen.onkeypress(self.turtle.move_down,"s")
        screen.onkeypress(self.turtle.move_right, "d")
        screen.onkeypress(self.turtle.move_left, "a")
        screen.listen()

class GUI:
    def __init__(self, turtle_name, tk_canvas):
        self.turtle_properties = turtle_name
        self.user_canvas = tk_canvas

    def build_box(self):
        screen_location = 1000
        screen_filler = screen_location*1.5
        frame = tk.Frame(canvas.master, bg="black", width=screen_filler, height=screen_filler)
        canvas.create_window(screen_location, 0, window=frame)
        frame = tk.Frame(canvas.master, bg="black", width=screen_filler, height=screen_filler)
        canvas.create_window(-screen_location, 0, window=frame)
        frame = tk.Frame(canvas.master, bg="black", width=screen_filler, height=screen_filler)
        canvas.create_window(0, screen_location, window=frame)
        frame = tk.Frame(canvas.master, bg="black", width=screen_filler, height=screen_filler)
        canvas.create_window(0, -screen_location, window=frame)


# this class handles the turtle that will be used for making the shape
class PointerTurtle:
    def __init__(self, turtle_name):
        # names the turtle we will be using and states where the turtle is
        self.pointer_turtle = turtle_name
        self.pointer_turtle.setundobuffer(255*255*255)
        self.pointer_turtle.speed(0)
        self.current_y = 0
        self.current_x = 0
        self.distance = 20
        # list for the tuples that will be saved later and used else where in the class
        self.tuple_list = []

    def __str__(self):
        # when called as a string I want to see the tuple list
        # to show the user the points they have saved
        return str(self.tuple_list)

    def undo_last(self):
        self.pointer_turtle.undo()

    def home(self):
        self.current_y = 0
        self.current_x = 0
        self.pointer_turtle.goto(self.current_x,self.current_y)

    def get_distance(self, answer):
        # sets distance travel to the input
        self.distance = int(answer)

    # for all of this the move code since turtle does not have a change x or y code
    # I have made it variables that it remembers and adds or subtracts to move
    def move_up(self):
        self.locate_thy_self()
        self.current_y = self.current_y + self.distance
        self.pointer_turtle.sety(self.current_y)
        self.pointer_turtle.speed(0)

    def move_down(self):
        self.locate_thy_self()
        self.current_y = self.current_y - self.distance
        self.pointer_turtle.sety(self.current_y)

    def move_right(self):
        self.locate_thy_self()
        self.current_x = self.current_x + self.distance
        self.pointer_turtle.setx(self.current_x)

    def move_left(self):
        self.locate_thy_self()
        self.current_x = self.current_x - self.distance
        self.pointer_turtle.setx(self.current_x)

    def save_tuple(self):
        # when saving a tuple I make the turtle make a dot of where it is
        # to remind the user where visually his shape will be
        self.locate_thy_self()
        width = int(round(self.distance/2, 0))
        self.pointer_turtle.dot(width, "blue")
        current_tuple = (self.current_x, self.current_y)
        self.tuple_list.append(current_tuple)

    def brush(self):
        self.pointer_turtle.speed(0)
        screen.onscreenclick(self.pointer_turtle.goto)

    def locate_thy_self(self):
        self.current_y = self.pointer_turtle.ycor()
        self.current_x = self.pointer_turtle.xcor()

    def tuple_of_tuples(self):
        # this just makes a tuple of the tuples so when it prints out the code
        # so the user knows not to touch it if they don't want to change the shape
        tuple_of_tuples = tuple(self.tuple_list)
        file = open("MyLittleTurtle.py", "w")
        file.write(f'import turtle\n'
                   f'Tuples = {tuple_of_tuples}\n'
                   f'turtle.mode("logo")\n'
                   f'turtle.begin_poly()\n'
                   f'for i in Tuples:\n'
                   f'    turtle.goto(i)\n'
                   f'turtle.end_poly()\n'
                   f'p = turtle.get_poly()\n'
                   f'turtle.register_shape("myFavouriteShape", p)\n'
                   f'turtle.shape("myFavouriteShape")\n'
                   f'turtle.goto(0, 0)\n'
                   f'turtle.clear()\n'
                   f'turtle.mainloop()')
        file.close()


if __name__ == '__main__':
    # if the name of the project is main it will run and use the classes
    # else the person looking at the code can snatch code from the classes
    # without running the program
    screen = t.Screen()
    canvas = screen.getcanvas()
    t.mode("logo")
    my_little_turtle = Turtle()
    Turtle = PointerTurtle(my_little_turtle)
    Controller = Controller(Turtle)
    Controller.main_loop()
    Turtle.brush()
    User_GUI = GUI(my_little_turtle, canvas)
    User_GUI.build_box()
    t.mainloop()