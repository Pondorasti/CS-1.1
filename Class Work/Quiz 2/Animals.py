class Animal:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "I am speaking"


class Cat(Animal):
    
    def speak(self):
        return "Meow"


class Dog(Animal):
    
    def speak(self):
        return "Bark"

animals = []
animals.append(Cat("Figaro"))
animals.append(Dog("Tervi"))

for animal in animals:
    print(animal.speak())


