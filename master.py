# this is a comments
import turtle as t
from turtle import Turtle

class Questionnaire:
    def __init__(self, turtle_name):
        self.turtle = turtle_name

    def start(self):
        question = ("You are able to move the turtle by writing 'up', 'down', 'left', and 'right'.\n"+
                    "If you want to make a point write 'point' or 'save'.\n"+
                    "If you wish to quit the program write 'quit' or ' break'\n")
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
        current_tuple = (self.current_x, self.current_y)
        self.tuple_list.append(current_tuple)


if __name__ == '__main__':
    screen = t.Screen()
    Turtle = PointerTurtle()
    App = Questionnaire(Turtle)
    App.start()
    t.mainloop()