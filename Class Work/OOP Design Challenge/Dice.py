from random import randint

class Dice(): 
    @staticmethod
    def roll():
        return randint(1, 5) + randint(1, 5)