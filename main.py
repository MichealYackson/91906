# Program written in python version 3.12
# This imports the libraries used by this code and what they need from it
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
        guidelines = (
            f'Here are the controls for the program:\n'
            "'WASD' or arrow keys is used for movement\n"
            "you can use 'Q' to make a tuple for your turtle shape.\n"
            "'Z' is to undo the last action you have done.\n"
            "Once you have a shape you can press 'ENTER' or 'L' to get your file.\n"
            "And you can close your program by pressing 'C'.\n"
            "pressing 'H' will return your turtle home (0,0).\n"
            "'E' will pause drawing the shape and 'R' will resume drawing it.\n"
            "Pressing 'I' will ask for the distance you want to travel.\n"
            "While pressing 'O' will ask to rename the turtles shape\n"
            "and pressing 'p' will ask you to rename the file you makes name.\n"
        )
        print(guidelines)
        screen.onkeypress(self.turtle.move_up, "w")
        screen.onkeypress(self.turtle.move_down, "s")
        screen.onkeypress(self.turtle.move_right, "d")
        screen.onkeypress(self.turtle.move_left, "a")
        screen.onkeypress(self.turtle.move_up, "Up")
        screen.onkeypress(self.turtle.move_down, "Down")
        screen.onkeypress(self.turtle.move_right, "Right")
        screen.onkeypress(self.turtle.move_left, "Left")
        screen.onkeyrelease(self.turtle.save_tuple, "q")
        screen.onkeypress(self.turtle.undo_last, "z")
        screen.onkeyrelease(self.turtle.make_file, "Return")
        screen.onkeyrelease(self.turtle.make_file, "l")
        screen.onkeyrelease(quit, "c")
        screen.onkeyrelease(self.turtle.home, "h")
        screen.onkeypress(self.turtle.pause_shape, "e")
        screen.onkeypress(self.turtle.resume_shape, "r")
        screen.onkeypress(self.ask_for_distance, "i")
        screen.onkeypress(self.ask_for_shape_name, "o")
        screen.onkeypress(self.ask_for_program_name, "p")
        screen.listen()

    def ask_for_distance(self):
        # Tells the turtle class how far it is allowed to move
        question = "What distance do you want to travel?\n"
        # Uses try except to avoid errors
        answer = input(question)
        try:
            answer = int(answer)
            self.turtle.get_distance(answer)
        except ValueError:
            print("Sorry that input wasn't valid, press 'i' to try again\n")

    def ask_for_program_name(self):
        # Tells the turtle class how far it is allowed to move
        question = "What do you want to name your file?\n"
        # Uses try except to avoid errors
        answer = input(question)
        self.turtle.set_file_name(answer)

    def ask_for_shape_name(self):
        # Tells the turtle class how far it is allowed to move
        question = "What do you want to name your shape?\n"
        # Uses try except to avoid errors
        answer = input(question)
        self.turtle.set_shape_name(answer)


class GUI:
    def __init__(self, turtle_name, tk_canvas, user_resolution):
        self.screen_location = user_resolution
        self.half_screen_location = self.screen_location / 2
        self.quarter_screen_location = self.screen_location / 4
        self.tenth_screen_location = self.screen_location / 10
        self.entry_and_text_width = int(round(
            int(round(self.tenth_screen_location / 10, 0)) * 1.5, 0
        ))
        self.special_height = -(self.quarter_screen_location + self.quarter_screen_location / 4)
        self.other_special_height = -(self.quarter_screen_location + self.quarter_screen_location / 2)
        self.user_font = "arial"

        self.turtle_properties = turtle_name
        self.user_canvas = tk_canvas

        self.distance_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.file_name_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.shape_name_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.red_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.blue_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.green_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.red_frame = tk.Frame(
            self.user_canvas.master,
            bg="red",
            width=self.tenth_screen_location,
            height=self.tenth_screen_location
        )
        self.blue_frame = tk.Frame(
            self.user_canvas.master,
            bg="blue",
            width=self.tenth_screen_location,
            height=self.tenth_screen_location
        )
        self.green_frame = tk.Frame(
            self.user_canvas.master,
            bg="green",
            width=self.tenth_screen_location,
            height=self.tenth_screen_location
        )
        self.rgb_frame = tk.Frame(
            self.user_canvas.master,
            bg="black",
            width=self.tenth_screen_location,
            height=self.tenth_screen_location
        )

    def build_frames(self):
        screen_filler = self.screen_location * 1.5
        box_colour = "dark grey"
        frame = tk.Frame(
            self.user_canvas.master,
            bg=box_colour,
            width=screen_filler,
            height=screen_filler
        )
        self.user_canvas.create_window(self.screen_location, 0, window=frame)
        frame = tk.Frame(
            self.user_canvas.master,
            bg=box_colour,
            width=screen_filler,
            height=screen_filler
        )
        self.user_canvas.create_window(-self.screen_location, 0, window=frame)
        frame = tk.Frame(
            self.user_canvas.master,
            bg=box_colour,
            width=screen_filler,
            height=screen_filler
        )
        self.user_canvas.create_window(0, self.screen_location, window=frame)
        frame = tk.Frame(
            self.user_canvas.master,
            bg=box_colour,
            width=screen_filler,
            height=screen_filler
        )
        self.user_canvas.create_window(0, -self.screen_location, window=frame)

        self.red_frame.lift()
        self.blue_frame.lift()
        self.green_frame.lift()
        self.rgb_frame.lift()
        self.user_canvas.create_window(
            -self.quarter_screen_location,
            self.other_special_height,
            window=self.red_frame
        )
        self.user_canvas.create_window(
            self.quarter_screen_location,
            self.other_special_height,
            window=self.blue_frame
        )
        self.user_canvas.create_window(
            0,
            self.other_special_height,
            window=self.green_frame
        )
        self.user_canvas.create_window(
            -self.half_screen_location,
            self.other_special_height,
            window=self.rgb_frame
        )

    def build_text_boxes(self):
        text_box = tk.StringVar()
        text_box.set(
            f'Here are the controls for the program:\n'
            "'WASD' or arrow keys is used for movement\n"
            "you can use 'Q' to make a tuple for your turtle shape.\n"
            "'Z' is to undo the last action you have done.\n"
            "Once you have a shape you can press 'ENTER' or 'L' to get your file.\n"
            "And you can close your program by pressing 'C'.\n"
            "pressing 'H' will return your turtle home (0,0).\n"
            "'E' will pause drawing the shape and 'R' will resume drawing it.\n"
            "Pressing 'I' will ask for the distance you want to travel.\n"
            "While pressing 'O' will ask to rename the turtles shape\n"
            "and pressing 'p' will ask you to rename the file you makes name.\n"
        )
        label = tk.Label(
            self.user_canvas.master,
            textvariable=text_box,
            font=(self.user_font, self.entry_and_text_width),
            wraplength=self.half_screen_location
        )
        self.user_canvas.create_window(
            -self.half_screen_location - self.tenth_screen_location,
            0,
            window=label
        )

    def build_gui_entries(self):
        self.red_entry.lift()
        self.blue_entry.lift()
        self.green_entry.lift()
        self.distance_entry.lift()
        self.file_name_entry.lift()
        self.shape_name_entry.lift()
        self.user_canvas.create_window(
            -self.quarter_screen_location,
            self.special_height,
            window=self.red_entry
        )
        self.user_canvas.create_window(
            self.quarter_screen_location,
            self.special_height,
            window=self.blue_entry
        )
        self.user_canvas.create_window(
            0,
            self.special_height,
            window=self.green_entry
        )
        self.user_canvas.create_window(
            self.half_screen_location + self.tenth_screen_location,
            0,
            window=self.distance_entry
        )
        self.user_canvas.create_window(
            self.half_screen_location + self.tenth_screen_location,
            -self.special_height - 2 * self.tenth_screen_location,
            window=self.file_name_entry
        )
        self.user_canvas.create_window(
            self.half_screen_location + self.tenth_screen_location,
            -self.special_height - self.tenth_screen_location,
            window=self.shape_name_entry
        )

    def build_gui_buttons(self):
        undo_button = tk.Button(
            canvas.master,
            text="Undo",
            font=(self.user_font, self.entry_and_text_width),
            command=self.turtle_properties.undo_last
        )
        make_point_button = tk.Button(
            canvas.master,
            text="Make Point",
            font=(self.user_font, self.entry_and_text_width),
            command=self.turtle_properties.save_tuple
        )
        home_button = tk.Button(
            canvas.master,
            text="Home",
            font=(self.user_font, self.entry_and_text_width),
            command=self.turtle_properties.home
        )
        quit_button = tk.Button(
            canvas.master,
            text="Quit",
            font=(self.user_font, self.entry_and_text_width),
            command=quit
        )
        pause_shape_button = tk.Button(
            canvas.master,
            text="Pause Shape",
            font=(self.user_font, self.entry_and_text_width),
            command=self.turtle_properties.pause_shape
        )
        resume_shape_button = tk.Button(
            canvas.master,
            text="Resume Shape",
            font=(self.user_font, self.entry_and_text_width),
            command=self.turtle_properties.resume_shape
        )
        distance_button = tk.Button(
            canvas.master,
            text="Set Distance",
            font=(self.user_font, self.entry_and_text_width),
            command=self.send_off_distance
        )
        make_program_button = tk.Button(
            canvas.master,
            text="Make Program",
            font=(self.user_font, self.entry_and_text_width),
            command=self.turtle_properties.make_file
        )
        clear_button = tk.Button(
            canvas.master,
            text="Clear",
            font=(self.user_font, self.entry_and_text_width),
            command=self.turtle_properties.clear
        )
        name_file_button = tk.Button(
            canvas.master,
            text="Name Program",
            font=(self.user_font, self.entry_and_text_width),
            command=self.name_file
        )
        shape_file_button = tk.Button(
            canvas.master,
            text="Name Shape",
            font=(self.user_font, self.entry_and_text_width),
            command=self.turtle_properties.set_shape_name
        )
        rgb_button = tk.Button(
            canvas.master,
            text="Submit Colours",
            font=(self.user_font, self.entry_and_text_width),
            command=self.send_off_colours
        )
        self.user_canvas.create_window(
            self.half_screen_location - self.tenth_screen_location,
            self.special_height,
            window=undo_button
        )
        self.user_canvas.create_window(
            self.half_screen_location - self.tenth_screen_location,
            self.special_height + 2 * self.tenth_screen_location,
            window=make_point_button
        )
        self.user_canvas.create_window(
            self.half_screen_location + self.tenth_screen_location,
            self.special_height + 2 * self.tenth_screen_location,
            window=home_button
        )
        self.user_canvas.create_window(
            self.half_screen_location + self.tenth_screen_location,
            self.special_height,
            window=quit_button
        )
        self.user_canvas.create_window(
            self.half_screen_location - self.tenth_screen_location,
            self.special_height + self.tenth_screen_location,
            window=pause_shape_button
        )
        self.user_canvas.create_window(
            self.half_screen_location + self.tenth_screen_location,
            self.special_height + self.tenth_screen_location,
            window=resume_shape_button
        )
        self.user_canvas.create_window(
            self.half_screen_location - self.tenth_screen_location,
            0,
            window=distance_button
        )
        self.user_canvas.create_window(
            self.half_screen_location - self.tenth_screen_location,
            -self.special_height,
            window=make_program_button
        )
        self.user_canvas.create_window(
            self.half_screen_location + self.tenth_screen_location,
            -self.special_height,
            window=clear_button
        )
        self.user_canvas.create_window(
            self.half_screen_location - self.tenth_screen_location,
            -self.special_height - 2 * self.tenth_screen_location,
            window=name_file_button
        )
        self.user_canvas.create_window(
            -self.half_screen_location,
            self.special_height,
            window=rgb_button
        )
        self.user_canvas.create_window(
            self.half_screen_location - self.tenth_screen_location,
            -self.special_height - self.tenth_screen_location,
            window=shape_file_button
        )

    def change_rgb_frame(self, red, green, blue):
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
        rgb_value = f'#{red:02x}{green:02x}{blue:02x}'
        self.rgb_frame = tk.Frame(
            self.user_canvas.master,
            bg=rgb_value,
            width=self.tenth_screen_location,
            height=self.tenth_screen_location
        )
        self.user_canvas.create_window(
            -self.half_screen_location,
            self.other_special_height,
            window=self.rgb_frame
        )

    def send_off_colours(self):
        screen.listen()
        red = self.red_entry.get()
        blue = self.blue_entry.get()
        green = self.green_entry.get()
        if red == "":
            red = "00"
        if blue == "":
            blue = "00"
        if green == "":
            green = "00"
        print(f'R:{red} G:{green} B:{blue}')
        self.turtle_properties.set_pen_colour(red, green, blue)
        self.change_rgb_frame(red, green, blue)

    def send_off_distance(self):
        screen.listen()
        distance = self.distance_entry.get()
        print(f'{distance}')
        self.turtle_properties.get_distance(distance)

    def name_file(self):
        screen.listen()
        file_name = self.file_name_entry.get()
        print(f'{file_name}')
        self.turtle_properties.set_file_name(file_name)


# This class handles the turtle that will be used for making the shape
class PointerTurtle:
    def __init__(self, turtle_name):
        # Names the turtle we will be using and states where the turtle is
        self.pointer_turtle = turtle_name
        self.pointer_turtle.setundobuffer(255 * 255 * 255)
        self.pointer_turtle.speed(0)
        self.current_y = 0
        self.current_x = 0
        self.pause_shape_x = 0
        self.pause_shape_y = 0
        self.distance = 20
        self.pointer_turtle_red = 0
        self.pointer_turtle_green = 0
        self.pointer_turtle_blue = 0
        # List for the tuples that will be saved later and used elsewhere in the class
        self.tuple_list = []
        self.file_name = "MyLittleTurtle"
        self.shape_name = "MyVeryOwnShape"
        self.history_of_actions = []
        self.movement_list_item = "movement action"

    def __str__(self):
        # When called as a string, show the tuple list to the user
        return str(self.tuple_list)

    def clear(self):
        self.current_y = 0
        self.current_x = 0
        self.pause_shape_x = 0
        self.pause_shape_y = 0
        self.distance = 20
        self.tuple_list = []
        self.file_name = "MyLittleTurtle"
        self.shape_name = "MyVeryOwnShape"
        self.pointer_turtle.clear()

    def undo_last(self):
        last_action = len(self.history_of_actions) - 1
        try:
            if self.history_of_actions[last_action] == "made tuple":
                self.tuple_list.pop()
        except:
            pass
        self.pointer_turtle.undo()
        self.history_of_actions.pop()

    def home(self):
        self.history_of_actions.append(self.movement_list_item)
        self.current_y = 0
        self.current_x = 0
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def get_distance(self, answer):
        # Sets distance travel to the input
        self.distance = int(answer)

    def move_up(self):
        self.locate_thy_self()
        self.current_y += self.distance
        self.pointer_turtle.sety(self.current_y)

    def move_down(self):
        self.locate_thy_self()
        self.current_y -= self.distance
        self.pointer_turtle.sety(self.current_y)

    def move_right(self):
        self.locate_thy_self()
        self.current_x += self.distance
        self.pointer_turtle.setx(self.current_x)

    def move_left(self):
        self.locate_thy_self()
        self.current_x -= self.distance
        self.pointer_turtle.setx(self.current_x)

    def save_tuple(self):
        # When saving a tuple, make a dot to mark the position
        self.locate_thy_self()
        self.history_of_actions.pop()
        self.history_of_actions.append("made tuple")
        width = int(round(self.distance / 2, 0))
        self.pointer_turtle.dot(width, "blue")
        current_tuple = (self.current_x, self.current_y)
        self.tuple_list.append(current_tuple)

    def brush(self):
        self.pointer_turtle.speed(0)
        screen.onscreenclick(self.click)

    def click(self, x, y):
        self.pointer_turtle.goto(x,y)
        self.history_of_actions.append(self.movement_list_item)

    def locate_thy_self(self):
        self.history_of_actions.append(self.movement_list_item)
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
        self.pointer_turtle_red = red
        self.pointer_turtle_green = green
        self.pointer_turtle_blue = blue
        self.pointer_turtle.pencolor(
            self.pointer_turtle_red,
            self.pointer_turtle_green,
            self.pointer_turtle_blue
        )
        self.pointer_turtle.color(
            self.pointer_turtle_red,
            self.pointer_turtle_green,
            self.pointer_turtle_blue
        )

    def pause_shape(self):
        self.pause_shape_y = self.pointer_turtle.ycor()
        self.pause_shape_x = self.pointer_turtle.xcor()
        self.pointer_turtle.pu()

    def resume_shape(self):
        current_x = self.pointer_turtle.xcor()
        current_y = self.pointer_turtle.ycor()
        self.pointer_turtle.goto(self.pause_shape_x, self.pause_shape_y)
        self.pointer_turtle.pd()
        self.pointer_turtle.goto(current_x, current_y)

    def set_file_name(self, name):
        self.file_name = name

    def set_shape_name(self, name):
        self.shape_name = name

    def make_file(self):
        # Creates a file with the turtle's shape data
        tuple_of_tuples = tuple(self.tuple_list)
        file = open(f'{self.file_name}.py', "w")
        file.write(
            f'import turtle\n'
            f'screen = turtle.Screen()\n'
            f'turtle.colormode(255)\n'
            f'turtle.mode("logo")\n'
            f'Tuples = {tuple_of_tuples}\n'
            f'{self.shape_name}_turtle = turtle.Turtle()\n'
            f'{self.shape_name}_turtle.color'
            f'({self.pointer_turtle_red}, {self.pointer_turtle_green}, {self.pointer_turtle_blue})\n'
            f'screen.register_shape("{self.shape_name}", Tuples)\n'
            f'{self.shape_name}_turtle.shape("{self.shape_name}")\n'
            f'turtle.mainloop()'
        )
        file.close()


def set_resolution():
    # function to get a desired width of the box that is the limits of the turtle for the program
    looping = True
    while looping:
        question = (
            f'How wide do you want to make your canvas for your turtle?\n'
            '(values between 500 to 1500 work nicely)\n'
        )
        answer = input(question)
        try:
            answer = int(answer)
            looping = False
        except:
            print("Sorry that input wasn't valid, please try again.\n")
    return answer # noqa


if __name__ == '__main__':
    # gets the total width of the turtle box
    resolution = set_resolution()
    # set screen to t.screen() object and a canvas for tkinter is assigned to it
    screen = t.Screen()
    canvas = screen.getcanvas()
    # sets up the turtle mode to "logo" and "colormode(255)" to better control the turtle and its colour
    t.mode("logo")
    t.colormode(255)
    # sets up a turtle for the rest of the program to use
    my_little_turtle = Turtle()
    # a class that adds additional functions to the turtle for easier use
    Turtle = PointerTurtle(my_little_turtle)
    # a class that allows for keyboard inputs to be used
    Controller = Controller(Turtle)
    Controller.main_loop()
    Turtle.brush()
    # a class that sets up the GUI that is used by the user
    User_GUI = GUI(Turtle, canvas, resolution)
    User_GUI.build_frames()
    User_GUI.build_text_boxes()
    User_GUI.build_gui_entries()
    User_GUI.build_gui_buttons()
    # Mainloop() finishes the initialisation of the program and is event driven afterward
    t.mainloop()