import turtle as t
import tkinter 

class Turtle(t.Turtle):  # Extend the original functionality of Turtle

    def smooth_goto(self, x, y):
        self.up()
        self.goto(x, y)
        self.down()

    def glow(self, x, y):
        self.fillcolor("black")

    def unglow(self, x, y):
        self.fillcolor("gray")

    __pen_instance = None
    __eraser = None

    @staticmethod
    def getInstance():  # Weak attempt at creating a Singleton
        if Turtle.__pen_instance == None:
            Turtle.__pen_instance = Turtle()

            Turtle.__create_pen_shape(Turtle.__pen_instance)
            Turtle.__pen_instance.shape("pen")

            Turtle.__pen_instance.speed(4)

        return Turtle.__pen_instance

    @staticmethod
    def __create_pen_shape(turtle):
        pen = Pen()
        pen_shape = pen.draw(turtle)
        turtle.clear()

        t.register_shape("pen", pen_shape)

    @staticmethod
    def prepare_for_drawing():
        pen = Turtle.getInstance()

        # Eraser
        eraser_shape = Eraser().draw(pen)

        t.register_shape("eraser", eraser_shape)
        eraser = Turtle()
        eraser.shape("eraser")

        eraser.smooth_goto(100, -200)
        eraser.unglow(100, -200)

        eraser.pencolor("white")
        eraser.pensize(5)

        eraser.onclick(eraser.glow)
        eraser.onrelease(eraser.unglow)

        eraser.speed(0)
        eraser.ondrag(eraser.goto)

        Turtle.__eraser = eraser

        # Pen
        pen.setheading(0)
        pen.smooth_goto(-100, -200)
        pen.unglow(-100, -200)

        pen.pencolor("black")
        pen.pensize(5)

        pen.onclick(pen.glow)
        pen.onrelease(pen.unglow)

        pen.speed(0)
        pen.ondrag(pen.goto)


class Pen:
    def __init__(self, tip_length = 20, pen_length = 80, color="", x=0, y=0):
        self.tip_length = tip_length
        self.pen_length = pen_length
        self.x = x
        self.y = y

    def draw(self, turtle=Turtle()):
        turtle.speed(0)
        turtle.smooth_goto(self.x, self.y)

        turtle.begin_poly()

        turtle.right(45)
        turtle.forward(self.tip_length)
        turtle.right(-45)
        turtle.forward(self.pen_length)

        turtle.smooth_goto(self.x, self.y)

        turtle.right(-45)
        turtle.forward(self.tip_length)
        turtle.right(45)
        turtle.forward(self.pen_length)

        turtle.end_poly()
        shape = turtle.get_poly()

        return shape


class Eraser:
    def __init__(self, width = 20, height = 80, color = "", x = 0, y = 0):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

    def draw(self, turtle = Turtle()):
        turtle.speed(0)
        turtle.smooth_goto(self.x, self.y)
        turtle.pencolor(self.color)

        turtle.begin_poly()

        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

        turtle.end_poly()
        shape = turtle.get_poly()

        return shape


class Flower:
    def __init__(self, num_petals, color, petal_length, petal_size, x, y):
        self.num_petals = num_petals
        self.color = color
        self.petal_length = petal_length
        self.petal_size = petal_size

        self.x = x
        self.y = y

    def __turn_degrees(self, num_petals):
        return 360 / num_petals

    def draw(self, turtle = Turtle.getInstance()):
        turtle.smooth_goto(self.x, self.y)

        turtle.pencolor(self.color)
        turtle.pensize(self.petal_size)

        for _ in range(self.num_petals):
            turtle.right(self.__turn_degrees(self.num_petals))
            turtle.forward(self.petal_length)
            turtle.goto(self.x, self.y)

        turtle.pencolor("orange")
        turtle.dot()
    
    def update(self, num_petals, color, petal_length, petal_size, x, y):
        self.num_petals = num_petals
        self.color = color
        self.petal_length = petal_length
        self.petal_size = petal_size
        self.x = x
        self.y = y


flower = Flower(6, "pink", 100, 40, 0, 0)

assert(flower._Flower__turn_degrees(6) == 60)

flower.draw()

flower.update(8, "red", 160, 30, 200, -100)
flower.draw()

flower.update(10, "blue", 80, 10, -300, 100)
flower.draw()

Turtle.prepare_for_drawing()

t.done()