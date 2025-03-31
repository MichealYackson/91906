# this imports the libraries used by this code and what they need from it
import turtle as t
from turtle import Turtle

class Controller:
    def __init__(self, turtle_name):
        self.turtle = turtle_name

    def main_loop(self):
        screen.onkeyrelease(self.turtle.save_tuple, "x")
        screen.onkeyrelease(self.turtle.tuple_of_tuples, "f")
        screen.onkeyrelease(quit, "q")
        screen.onkeyrelease(self.turtle.home, "h")
        screen.onkeyrelease(self.turtle.undo_last, "z")
        screen.onkeypress(self.turtle.move_up,"w")
        screen.onkeypress(self.turtle.move_down,"s")
        screen.onkeypress(self.turtle.move_right, "d")
        screen.onkeypress(self.turtle.move_left, "a")
        screen.listen()



# this class handles the turtle that will be used for making the shape
class PointerTurtle:
    def __init__(self):
        # names the turtle we will be using and states where the turtle is
        self.pointer_turtle = Turtle()
        self.pointer_turtle.setundobuffer(255*255*255)
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
        self.pointer_turtle.goto(0,0)

    def get_distance(self, answer):
        # sets distance travel to the input
        self.distance = int(answer)

    # for all of this the move code since turtle does not have a change x or y code
    # I have made it variables that it remembers and adds or subtracts to move
    def move_up(self):
        self.current_y = self.current_y + self.distance
        self.pointer_turtle.sety(self.current_y)

    def move_down(self):
        self.current_y = self.current_y - self.distance
        self.pointer_turtle.sety(self.current_y)

    def move_right(self):
        self.current_x = self.current_x + self.distance
        self.pointer_turtle.setx(self.current_x)

    def move_left(self):
        self.current_x = self.current_x - self.distance
        self.pointer_turtle.setx(self.current_x)

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
    t.mode("logo")
    Turtle = PointerTurtle()
    App = Controller(Turtle)
    App.main_loop()
    t.mainloop()
