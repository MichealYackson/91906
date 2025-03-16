# this is a comment
import turtle as t
from turtle import Turtle

class Questionnaire:
    def __init__(self, turtle_name):
        self.turtle = turtle_name

    def start(self):
        start = True
        while start == True:
            question = "Which direction do you want to move in?"
            answer = (input(question)).lower()
            if answer == "up":
                self.turtle.move_up()
            elif answer == "down":
                self.turtle.move_down()
            elif answer == "right":
                self.turtle.move_right()
            elif answer == "left":
                self.turtle.move_left()
            else:
                start = False


class PointerTurtle:
    def __init__(self):
        self.pointer_turtle = Turtle()
        self.current_y = 0
        self.current_x = 0

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


if __name__ == '__main__':
    screen = t.Screen()
    Turtle = PointerTurtle()
    App = Questionnaire(Turtle)
    App.start()
    t.mainloop()