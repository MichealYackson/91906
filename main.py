# this imports the libraries used by this code and what they need from it
import turtle as t
from turtle import Turtle

""" makes the questionnaire class used for asking what direction the user wants to
move in and if the user wants to quit the program or if they want to makes spots
or if they want the code using a large if else tree"""
class Questionnaire:
    def __init__(self, turtle_name):
        #just sets the turtles name we are using for this program
        self.turtle = turtle_name

    def start(self):
        # tells the users what inputs they can use during the running of the program
        question = ("You are able to move the turtle by writing 'up', 'down', 'left', and 'right'.\n"+
                    "If you want to make a point write 'point' or 'save'.\n"+
                    "If you wish to quit the program write 'quit' or ' break'\n"+
                    "If you wish to print out the code for your tuples write 'code' or 'tuples'\n"
                    "You can change the scale of the distance you travel "
                    "(default distance is 20) at any time by typing 'scale' or 'size'\n")
        # calls the main loop of the program
        print(question)
        self.questioning()

    def questioning(self):
        # I use a while loop with only string inputs on a large if else tree to see what they want to do
        start = True
        while start == True:
            question = "What do you want to do?\n"
            answer = (input(question)).lower()
            # next 4 if else's just tell the other class handling the turtle where to move
            if answer == "up":
                self.turtle.move_up()
            else:
                if answer == "down":
                    self.turtle.move_down()
                else:
                    if answer == "right":
                        self.turtle.move_right()
                    else:
                        if answer == "left":
                            self.turtle.move_left()
                        else:
                            if answer == "quit" or answer == "break":
                                start = False
                                quit()
                                break
                            else:
                                if answer == "code" or answer == "tuples" or answer == "tuple":
                                    # gets the code for the user from the other class
                                    self.turtle.tuple_of_tuples()
                                else:
                                    if answer == "point" or answer == "save" or answer == "save point":
                                        # tells the other class to save the tuple they are on
                                        self.turtle.save_tuple()
                                        print(self.turtle)
                                    else:
                                        if answer == "size" or answer == "scale" or answer == "distance":
                                            question = "What distance do you want to travel?\n"
                                            answer = input(question)
                                            try:
                                                answer = int(answer)
                                                self.turtle.get_distance(answer)
                                            except ValueError:
                                                print("Sorry that input wasn't valid")
                                        else:
                                            print("Sorry that input wasn't valid")


# this class handles the turtle that will be used for making the shape
class PointerTurtle:
    def __init__(self):
        # names the turtle we will be using and states where the turtle is
        self.pointer_turtle = Turtle()
        self.current_y = 0
        self.current_x = 0
        self.distance = 20
        # list for the tuples that will be saved later and used else where in the class
        self.tuple_list = []

    def __str__(self):
        # when called as a string I want to see the tuple list
        # to show the user the points they have saved
        return str(self.tuple_list)

    def get_distance(self, answer):
            self.distance = int(answer)

    # for all of the move code since turtle does not have a change x or y code
    # I have made it variables that it remembers and adds or subtracts to move
    def move_up(self):
        self.current_y = self.current_y + self.distance
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def move_down(self):
        self.current_y = self.current_y - self.distance
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def move_right(self):
        self.current_x = self.current_x + self.distance
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def move_left(self):
        self.current_x = self.current_x - self.distance
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def save_tuple(self):
        # when saving a tuple I make the turtle make a dot of where it is
        # to remind the user where visually his shape will be
        width = int(round(self.distance/2, 0))
        self.pointer_turtle.dot(width, "blue")
        current_tuple = (self.current_x, self.current_y)
        self.tuple_list.append(current_tuple)

    def tuple_of_tuples(self):
        # this just makes a tuple of the tuples so when it prints out the code
        # so the user knows not to touch it if they don't want to change the shape
        tuple_of_tuples = tuple(self.tuple_list)
        print(f'import turtle\n'
              f'Tuples = {tuple_of_tuples}\n'
              f'turtle.mode("logo")\n'
              f'turtle.begin_poly()\n'
              f'for i in (Tuples):\n'
              f'    turtle.goto(i)\n'
              f'turtle.end_poly()\n'
              f'p = turtle.get_poly()\n'
              f'turtle.register_shape("myFavouriteShape", p)\n'
              f'turtle.shape("myFavouriteShape")\n'
              f'turtle.goto(0, 0)\n'
              f'turtle.clear')


if __name__ == '__main__':
    # if the name of the project is main it will run and use the classes
    # else the person looking at the code can snatch code from the classes
    # without running the program
    screen = t.Screen()
    Turtle = PointerTurtle()
    App = Questionnaire(Turtle)
    App.start()
    t.mainloop()