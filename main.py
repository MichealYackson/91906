# Program written in python version 3.12
# This imports the libraries used by this code and what they need from it
import turtle as t
import tkinter as tk
from turtle import Turtle
from tkinter import ttk

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
            if answer > 1500:
                    print("Sorry that number is too big")
            else:
                if answer < 500:
                    print("Sorry that number is too small")
                else:
                    looping = False
        except KeyboardInterrupt:
            exit()
        except ValueError:
            print("Sorry that input wasn't valid, please try again with a number.\n")
    return answer # noqa

def check_colour_value(colour):
    # checks the colour value of the colour pickers entries
    # method does not require self values and therefore does not have to be within the class
    try:
        colour = float(colour)
        colour = int(round(colour, 0))
        if colour > 255:
                print("Sorry that number is too big for a colour.\n"
                      "try a value between 0 and 255.")
                colour = 255
        else:
            if colour < 0:
                print("Sorry that number is too small for a colour.\n"
                      "try a value between 0 and 255.")
                colour = 0
            else:
                pass
    except ValueError:
        if colour == "":
            colour = 0
        else:
            print("An exception occurred, please try again with a number between 0 and 255.")
            colour = 0
    return colour

class Controller:
    def __init__(self, turtle_name):
        # this lets the Controller use the other classes functions
        self.turtle = turtle_name

    def main_loop(self):
        # Prints out instructions in the command line
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
        # Binds all the key presses to functions using screen onkey press or release
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
        # listen() is used to bring focus back to the screen instead of the command line or tk widgets
        screen.listen()

    def ask_for_distance(self):
        # Tells the turtle class how far it is allowed to move
        question = "What distance do you want to travel?\n"
        # Uses try except to avoid errors
        answer = input(question)
        try:
            answer = float(answer)
            answer = int(round(answer, 0))
            self.turtle.get_distance(answer)
        except KeyboardInterrupt:
            exit()
        except ValueError:
            print("Sorry that input wasn't valid, press 'i' to try again\n")

    def ask_for_program_name(self):
        # tells the turtle what to name the program
        question = "What do you want to name your file?\n"
        illegal_characters = ["#", "%", "&", "{", "}", "\\", "<", ">",
                              "*", "?", "/", " ", "$", "!", '"', "'", ":",
                              "@", "+", "`", "|", "="]
        answer = input(question)

        # Remove all illegal characters from the answer
        cleaned_answer = ''.join([char for char in answer if char not in illegal_characters])

        if cleaned_answer != answer:
            print(f"Sorry, your input contained illegal characters. They have been removed.\n"
                  f"Here is the cleaned filename: {cleaned_answer}\n"
                  f"Here is a list of illegal characters: {illegal_characters}")
            answer = cleaned_answer  # Use the cleaned version

        self.turtle.set_file_name(answer)

    def ask_for_shape_name(self):
        # Tells the turtle class what to name the shape
        question = "What do you want to name your shape?\n"
        answer = input(question)
        self.turtle.set_shape_name(answer)


class GUI:
    def __init__(self, turtle_name, tk_canvas, user_resolution):
        # changeable variables used throughout the class
        # screen location allows for easy adjustable scaling of tk widgets
        self.screen_location = user_resolution
        self.half_screen_location = self.screen_location / 2
        self.quarter_screen_location = self.screen_location / 4
        self.tenth_screen_location = self.screen_location / 10
        self.entry_and_text_width = int(round(
            int(round(self.tenth_screen_location / 10, 0)) * 1.5, 0
        ))
        self.special_height = -(self.quarter_screen_location + self.quarter_screen_location / 4)
        self.other_special_height = -(self.quarter_screen_location + self.quarter_screen_location / 2)
        self.user_font = "Comic sans ms"

        # calling the frame to be easily used for tk widgets
        # also calls the class that controls and manages the turtle to add more functionality to the widgets
        self.turtle_properties = turtle_name
        self.user_canvas = tk_canvas

        # states the entries to be later used in multiple functions so they have to be callable anywhere in the class
        self.distance_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.file_name_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.shape_name_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.red_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.blue_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)
        self.green_entry = ttk.Entry(self.user_canvas.master, width=self.entry_and_text_width)

        # frames can change colour and therefore need to be used in multiple functions like the entries
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
        # this function is used to build the frame where the turtle is kept
        # screen filler is a variable used to determine the sizes of the frames since we can not use fill
        # since we are not packing the widgets in just with tkinter
        screen_filler = self.screen_location * 1.5
        box_colour = "dark grey"
        # places 4 different frames around to give a nice square empty box for the turtle to make a shape
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
        # this function states what mainloop does but in a tk label for easier visual use
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
        # this function places the entries around the screen
        # .lift() entry lifts all the entries to the front after build_frames covers them with frames
        self.red_entry.lift()
        self.blue_entry.lift()
        self.green_entry.lift()
        self.distance_entry.lift()
        self.file_name_entry.lift()
        self.shape_name_entry.lift()
        # places the entries on the canvas that were created in __init__
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
        # this function places down all the buttons down on the screen
        # this function creates all the buttons because they do not need to be in the __init__
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
            command=self.turtle_properties.clear_turtle
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
        # this section places down all the buttons
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
        # this function changes the colour of the black frame to what the user has set from the rgb picker
        red = check_colour_value(red)
        green = check_colour_value(green)
        blue = check_colour_value(blue)
        # rgb_value converts the 16bit colour to hex
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
        # this function get the inputs from the entries and sends it off to change
        # the turtles colour and the tkinter frames colour
        # screen.listen() changes the focus from the entries back to the turtle screen
        screen.listen()
        red = check_colour_value(self.red_entry.get())
        blue = check_colour_value(self.blue_entry.get())
        green = check_colour_value(self.green_entry.get())
        self.turtle_properties.set_pen_colour(red, green, blue)
        self.change_rgb_frame(red, green, blue)

    def send_off_distance(self):
        # gets the distance the user has input into the entry and sends it off to the turtle to handle
        # screen.listen() changes the focus from the entries back to the turtle screen
        screen.listen()
        distance = self.distance_entry.get()
        self.turtle_properties.get_distance(distance)

    def name_file(self):
        # gets the name the user has input into the entry and sends it off to the turtle to handle
        # screen.listen() changes the focus from the entries back to the turtle screen
        screen.listen()
        file_name = self.file_name_entry.get()
        illegal_characters = ["#", "%", "&", "{", "}", "\\", "<", ">",
                              "*", "?", "/", " ", "$" ,"!", '"', "'", ":",
                              "@", "+", "`", "|", "="]
        # Remove all illegal characters from the answer
        cleaned_file_name = ''.join([char for char in file_name if char not in illegal_characters])

        if cleaned_file_name != file_name:
            print(f"Sorry, your input contained illegal characters. They have been removed.\n"
                  f"Here is the cleaned filename: {cleaned_file_name}\n"
                  f"Here is a list of illegal characters:\n {illegal_characters}")
            file_name = cleaned_file_name  # Use the cleaned version

        self.turtle_properties.set_file_name(file_name)


class PointerTurtle:
    def __init__(self, turtle_name, shape_size):
        # Names the turtle we will be using and states where the turtle is
        self.screen_size = shape_size/5
        self.pointer_turtle = turtle_name
        self.pointer_turtle.setundobuffer(255 * 255 * 255)
        self.pointer_turtle.speed(0)
        self.pointer_turtle.shape("classic")
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
        self.history_of_actions = ["set properties after undo"]
        self.movement_list_item = "movement action"
        screen.onscreenclick(self.click)

    def __str__(self):
        # When called as a string, show the tuple list to the user
        return str(self.tuple_list)

    def clear_turtle(self):
        # essentially resets the location and tuple variables back to what they were in the __init__ for a fresh slate
        self.home()
        self.tuple_list = []
        self.pointer_turtle.clear()

    def undo_last(self):
        # undoes the last movement action or tuple action
        last_action = len(self.history_of_actions) - 1
        try:
            # if an undo was last did it will first get rid of it before checking for anything else
            if self.history_of_actions[last_action] == "set properties after undo":
                for i in range(3):
                    self.pointer_turtle.undo()
                self.history_of_actions.pop()
                last_action = len(self.history_of_actions) - 1
        except IndexError:
            pass
        try:
            # then it checks if the colour picker was used to undo the colour change enough times for
            # turtle undogoto to occur, does not always work but is much more reliable than not having it
            while self.history_of_actions[last_action] == "changed colour":
                print(self.history_of_actions[last_action])
                self.pointer_turtle.undo()
                self.history_of_actions.pop()
                last_action = len(self.history_of_actions) - 1
                print(self.history_of_actions[last_action])
        except IndexError:
            pass
        try:
            # checks if a tuple was made during the last action and deletes it if is point was undone
            if self.history_of_actions[last_action] == "made tuple":
                self.tuple_list.pop()
        except IndexError:
            pass
        try:
            # has to undo 5 to move back correctly because of the turtle functions it does
            for i in range(5):
                self.pointer_turtle.undo()
            self.history_of_actions.pop()
        except IndexError:
            pass
        self.set_turtle_colour_properties()
        self.history_of_actions.append("set properties after undo")

    def move_turtle(self):
        # changes the turtles direction it faces and makes it go there
        heading = self.pointer_turtle.towards(self.current_x, self.current_y)
        self.pointer_turtle.seth(heading)
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def home(self):
        # returns the turtle  back to the centre of the shape and canvas
        self.history_of_actions.append(self.movement_list_item)
        self.current_y = 0
        self.current_x = 0
        self.move_turtle()
        self.pointer_turtle.seth(0)

    def get_distance(self, answer):
        # Sets distance travel to the input
        self.distance = int(answer)

    def move_up(self):
        # moves up the turtle the set distance
        self.locate_thy_self()
        self.current_y += self.distance
        self.move_turtle()

    def move_down(self):
        # moves down the turtle the set distance
        self.locate_thy_self()
        self.current_y -= self.distance
        self.move_turtle()


    def move_right(self):
        # moves the turtle to the right the set distance
        self.locate_thy_self()
        self.current_x += self.distance
        self.move_turtle()

    def move_left(self):
        # moves the turtle to the left the set distance
        self.locate_thy_self()
        self.current_x -= self.distance
        self.move_turtle()

    def save_tuple(self):
        # When saving a tuple, make a dot to mark the position
        self.locate_thy_self()
        self.history_of_actions.pop()
        self.history_of_actions.append("made tuple")
        width = int(round(self.distance / 2, 0))
        self.pointer_turtle.dot(width, "black")
        current_tuple = (self.current_x, self.current_y)
        self.tuple_list.append(current_tuple)

    def click(self, x, y):
        # when the screen is clicked it will move the turtle there and add that movement to the history_of_actions
        self.current_x = x
        self.current_y = y
        self.move_turtle()
        self.locate_thy_self()

    def locate_thy_self(self):
        # before the turtle moves it has to locate itself before it does so to prevent any erros from happening
        # due to the ability to click anywhere on the screen and for WASD controls to be used at the same time
        self.history_of_actions.append(self.movement_list_item)
        self.current_y = self.pointer_turtle.ycor()
        self.current_x = self.pointer_turtle.xcor()
        self.set_turtle_colour_properties()
        """ this section doesn't work when clicking on the screen
         this error could be due to goto as speed 0 not being fast enough for the turtle to notice it has gone
         beyond the dedicated borders. a fix could be to teleport the turtle first and then drag it back from its
         original location to there to make sure it gets the right cords before drawing"""
        if self.screen_size < self.current_y:
            self.current_y = self.screen_size
        if self.screen_size < self.current_x:
            self.current_x = self.screen_size
        if -self.screen_size > self.current_y:
            self.current_y = -self.screen_size
        if -self.screen_size > self.current_x:
            self.current_x = -self.screen_size

    def set_pen_colour(self, red, green, blue):
        # Sets the pen and fill colour of the turtle to that of the colour picker
        self.pointer_turtle_red = red
        self.pointer_turtle_green = green
        self.pointer_turtle_blue = blue
        self.set_turtle_colour_properties()
        self.history_of_actions.append("changed colour")

    def set_turtle_colour_properties(self):
        self.pointer_turtle.pensize(1)
        self.pointer_turtle.speed(0)
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
        # pauses the turtles movement and allows for greater precision
        self.pause_shape_y = self.pointer_turtle.ycor()
        self.pause_shape_x = self.pointer_turtle.xcor()
        self.pointer_turtle.pu()

    def resume_shape(self):
        # resumes the turtles movement and allows for greater precision
        current_x = self.pointer_turtle.xcor()
        current_y = self.pointer_turtle.ycor()
        self.pointer_turtle.goto(self.pause_shape_x, self.pause_shape_y)
        self.pointer_turtle.pd()
        self.pointer_turtle.goto(current_x, current_y)

    def set_file_name(self, name):
        # changes the name of the file
        self.file_name = name

    def set_shape_name(self, name):
        # changes the name of the turtle shape being made
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
    Turtle = PointerTurtle(my_little_turtle, resolution)
    # a class that allows for keyboard inputs to be used
    Controller = Controller(Turtle)
    Controller.main_loop()
    # a class that sets up the GUI that is used by the user
    User_GUI = GUI(Turtle, canvas, resolution)
    User_GUI.build_frames()
    User_GUI.build_text_boxes()
    User_GUI.build_gui_entries()
    User_GUI.build_gui_buttons()
    # Mainloop() finishes the initialisation of the program and is event driven afterward
    t.mainloop()