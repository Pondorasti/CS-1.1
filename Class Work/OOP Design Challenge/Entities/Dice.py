from random import randint
from abc import ABC, abstractmethod

class Dice(ABC): 
    @abstractmethod
    def __init__(self):
        pass

    @staticmethod
    def roll():
        return randint(1, 5) + randint(1, 5)