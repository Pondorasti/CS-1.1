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



class Pen:
    def __init__(self, tip_length=20, pen_length=80):
        self.tip_length = tip_length
        self.pen_length = pen_length

    def draw(self, jerry=Turtle()):
        jerry.speed(0)
        jerry.smooth_goto(0, 0)

        jerry.begin_poly()

        jerry.right(45)
        jerry.forward(self.tip_length)
        jerry.right(-45)
        jerry.forward(self.pen_length)

        jerry.smooth_goto(0, 0)

        jerry.right(-45)
        jerry.forward(self.tip_length)
        jerry.right(45)
        jerry.forward(self.pen_length)

        jerry.end_poly()
        pen_shape = jerry.get_poly()

        return pen_shape



class Jerry:  # Weak attempt at creating a Singleton
    __instance = None

    @staticmethod
    def getInstance():
        if Jerry.__instance == None:
            Jerry.__instance = Turtle()

            Jerry.__create_pen_shape(Jerry.__instance)
            Jerry.__instance.shape("pen")

            Jerry.__instance.speed(4)

        return Jerry.__instance

    @staticmethod
    def __create_pen_shape(jerry):
        pen = Pen()
        pen_shape = pen.draw(jerry)
        jerry.clear()

        t.register_shape("pen", pen_shape)

    @staticmethod
    def prepare_for_drawing():
        jerry = Jerry.getInstance()

        jerry.smooth_goto(0, -200)
        jerry.unglow(0, -200)

        jerry.pencolor("white")
        jerry.pensize(5)

        jerry.onclick(jerry.glow)
        jerry.onrelease(jerry.unglow)

        jerry.speed(0)
        jerry.ondrag(jerry.goto)


class Flower:
    def __init__(self, num_petals, color, petal_length, petal_size, x, y):
        self.num_petals = num_petals
        self.color = color
        self.petal_length = petal_length
        self.petal_size = petal_size

        self.x = x
        self.y = y

    def __turn_degrees(self, num_petals):
        return 360/num_petals

    def draw(self, jerry=Jerry.getInstance()):
        jerry.smooth_goto(self.x, self.y)

        jerry.pencolor(self.color)
        jerry.pensize(self.petal_size)

        for _ in range(self.num_petals):
            jerry.right(self.__turn_degrees(self.num_petals))
            jerry.forward(self.petal_length)
            jerry.goto(self.x, self.y)

        jerry.pencolor("orange")
        jerry.dot()



    

myFlower = Flower(6, "pink", 100, 40, 0, 0)
myFlower.draw()


Jerry.prepare_for_drawing()

t.done()

# input("Press any key to exit... ")
