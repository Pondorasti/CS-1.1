import turtle

class Jerry: # Weak attempt at creating a Singleton
    _instance = None

    @staticmethod
    def getInstance():
        if Jerry._instance == None:
            print("poof")
            Jerry._instance = turtle.Turtle()
        return Jerry._instance

class Flower:
    def __init__(self, num_petals, color, petal_length, petal_size, x, y):
        self.num_petals = num_petals
        self.color = color
        self.petal_length = petal_length
        self.petal_size = petal_size

        self.x = x
        self.y = y

    def turn_degrees(self, num_petals):
        return 360/num_petals

    def draw(self):
        
        jerry = Jerry.getInstance()

        jerry.up()
        jerry.goto(self.x, self.y)
        jerry.down()

        jerry.speed(1)
        jerry.shape("turtle")

        jerry.pencolor(self.color)
        jerry.pensize(self.petal_size)

        for _ in range(self.num_petals):
            jerry.goto(self.x, self.y)
            jerry.right(self.turn_degrees(self.num_petals))
            jerry.forward(self.petal_length)

        jerry.dot()


myFlower = Flower(6, "pink", 100, 40, 0, 0)
myFlower.draw()

input("Press any key to exit... ")
