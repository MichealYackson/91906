# this is a comments
import turtle as t
from turtle import Turtle

class Questionnaire:
    def __init__(self, turtle_name):
        self.turtle = turtle_name

    def start(self):
        question = ("You are able to move the turtle by writing 'up', 'down', 'left', and 'right'.\n"+
                    "If you want to make a point write 'point' or 'save'.\n"+
                    "If you wish to quit the program write 'quit' or ' break'\n"+
                    "If you wish to print out the code for your tuples write 'code' or 'tuples'\n")
        print(question)
        self.questioning()

    def questioning(self):
        start = True
        while start == True:
            question = "What do you want to do?\n"
            answer = (input(question)).lower()
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
                                    self.turtle.tuple_of_tuples()
                                else:
                                    if answer == "point" or answer == "save" or answer == "save point":
                                        self.turtle.save_tuple()
                                        print(self.turtle)
                                    else:
                                        print("Sorry that input wasn't valid")



class PointerTurtle:
    def __init__(self):
        self.pointer_turtle = Turtle()
        self.current_y = 0
        self.current_x = 0
        self.tuple_list = []

    def __str__(self):
        return str(self.tuple_list)

    def move_up(self):
        self.current_y = self.current_y + 20
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def move_down(self):
        self.current_y = self.current_y - 20
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def move_right(self):
        self.current_x = self.current_x + 20
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def move_left(self):
        self.current_x = self.current_x - 20
        self.pointer_turtle.goto(self.current_x, self.current_y)

    def save_tuple(self):
        self.pointer_turtle.dot(10, "blue")
        current_tuple = (self.current_x, self.current_y)
        self.tuple_list.append(current_tuple)

    def tuple_of_tuples(self):
        tuple_of_tuples = tuple(self.tuple_list)
        print(tuple_of_tuples)
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
    screen = t.Screen()
    Turtle = PointerTurtle()
    App = Questionnaire(Turtle)
    App.start()
    t.mainloop()