# this imports the libraries used by this code and what they need from it
import turtle as t
import tkinter as tk
from contextlib import nullcontext
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
        self.screen_location = 1000
        self.half_screen_location = self.screen_location / 2
        self.quarter_screen_location = self.screen_location / 4
        self.tenth_screen_location = self.screen_location / 10
        self.entry_width = int(round(self.tenth_screen_location/10, 0))

        self.turtle_properties = turtle_name
        self.user_canvas = tk_canvas

        self.intro_text_box = tk.StringVar()
        self.red_entry = ttk.Entry(self.user_canvas.master, width=self.entry_width)
        self.blue_entry = ttk.Entry(self.user_canvas.master, width=self.entry_width)
        self.green_entry = ttk.Entry(self.user_canvas.master, width=self.entry_width)
        self.rgb_submit = tk.Button(canvas.master, text="Submit Colours", command=self.send_off_colours)
        self.red_frame = tk.Frame(self.user_canvas.master, bg="red", width=self.tenth_screen_location,
                                  height=self.tenth_screen_location)
        self.blue_frame = tk.Frame(self.user_canvas.master, bg="blue", width=self.tenth_screen_location,
                                  height=self.tenth_screen_location)
        self.green_frame = tk.Frame(self.user_canvas.master, bg="green", width=self.tenth_screen_location,
                                  height=self.tenth_screen_location)
        self.rgb_frame = tk.Frame(self.user_canvas.master, bg="black", width=self.tenth_screen_location,
                                  height=self.tenth_screen_location)


    def build_box(self):
        screen_filler = self.screen_location*1.5
        box_colour= "dark grey"
        frame = tk.Frame(self.user_canvas.master, bg=box_colour, width=screen_filler, height=screen_filler)
        self.user_canvas.create_window(self.screen_location, 0, window=frame)
        frame = tk.Frame(self.user_canvas.master, bg=box_colour, width=screen_filler, height=screen_filler)
        self.user_canvas.create_window(-self.screen_location, 0, window=frame)
        frame = tk.Frame(self.user_canvas.master, bg=box_colour, width=screen_filler, height=screen_filler)
        self.user_canvas.create_window(0, self.screen_location, window=frame)
        frame = tk.Frame(self.user_canvas.master, bg=box_colour, width=screen_filler, height=screen_filler)
        self.user_canvas.create_window(0, -self.screen_location, window=frame)

    def build_intro_text_box(self):
        self.intro_text_box.set("Here are the controls for the program:\n"
                      "*'WASD' is used for movement\n"
                      "*you can use 'Q' to make a tuple for your turtle shape.\n"
                      "*'R' is to undo the last action you have done\n"
                      "*Once you have a shape you can press 'ENTER' to get your file\n"
                      "*And you can close your program by pressing 'C'\n")
        label = tk.Label(self.user_canvas.master, textvariable=self.intro_text_box, wraplength=self.quarter_screen_location)
        self.user_canvas.create_window(-self.half_screen_location, 0, window=label)

    def build_gui_controller(self):
        self.red_entry.lift()
        self.blue_entry.lift()
        self.green_entry.lift()
        self.rgb_submit.lift()
        self.red_frame.lift()
        self.blue_frame.lift()
        self.green_frame.lift()
        self.rgb_frame.lift()
        special_height = -(self.quarter_screen_location + self.quarter_screen_location/4)
        other_special_height = -(self.quarter_screen_location + self.quarter_screen_location/2)
        self.user_canvas.create_window(-self.quarter_screen_location, special_height, window=self.red_entry)
        self.user_canvas.create_window(self.quarter_screen_location,special_height, window=self.blue_entry)
        self.user_canvas.create_window(0, special_height, window=self.green_entry)
        self.user_canvas.create_window(other_special_height, special_height, window=self.rgb_submit)
        self.user_canvas.create_window(-self.quarter_screen_location, other_special_height, window=self.red_frame)
        self.user_canvas.create_window(self.quarter_screen_location, other_special_height, window=self.blue_frame)
        self.user_canvas.create_window(0, other_special_height, window=self.green_frame)
        self.user_canvas.create_window(other_special_height, other_special_height, window=self.rgb_frame)

    def other_buttons(self):
        undo_button = tk.Button(canvas.master, text="Undo", command=self.turtle_properties.undo_last)
        make_point_button = tk.Button(canvas.master, text="Make Point", command=self.turtle_properties.save_tuple())
        home_button = tk.Button(canvas.master, text="Home", command=self.turtle_properties.home())
        quit_button = tk.Button(canvas.master, text="Quit", command=quit)
        distance_button = tk.Button(canvas.master, text="Set Distance", command=self.send_off_distance())
        code_button = tk.Button(canvas.master, text="Make Program", command=self.turtle_properties.tuple_of_tuples())


    def send_off_colours(self):
        red = self.red_entry.get()
        blue = self.blue_entry.get()
        green = self.green_entry.get()
        if red == "":
            red = "0"
        if blue == "":
            blue = "0"
        if green == "":
            green = "0"
        print(f'R:{red} G:{green} B:{blue}')
        self.turtle_properties.set_pen_colour(red,green,blue)

    def send_off_distance(self):
        pass





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

    def set_pen_colour(self, red, green, blue):
        try:
            red = int(red)
        except:
            print("An exception occurred")
            red = 0
        try:
            green = int(green)
        except:
            print("An exception occurred")
            green = 0
        try:
            blue = int(blue)
        except:
            print("An exception occurred")
            blue = 0
        self.pointer_turtle.pencolor(red, green, blue)


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
    t.colormode(255)
    my_little_turtle = Turtle()
    Turtle = PointerTurtle(my_little_turtle)
    Controller = Controller(Turtle)
    Controller.main_loop()
    Turtle.brush()
    User_GUI = GUI(Turtle, canvas)
    User_GUI.build_box()
    User_GUI.build_intro_text_box()
    User_GUI.build_gui_controller()
    t.mainloop()