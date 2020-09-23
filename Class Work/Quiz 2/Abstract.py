from abc import ABC, abstractmethod

class Eatable(ABC):
    def __init__(self, calories, proteins, fat):
        self.calories = calories
        self.proteins = proteins
        self.fat = fat
    
    @abstractmethod 
    def eat(self):
        pass

class Cereal(Eatable):
    def eat(self):
        print("Don't forget the milk!")
        print("Chomp Chomp")


captainCrunch = Cereal(100, 0, 20)
captainCrunch.eat()
