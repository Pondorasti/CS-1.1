class Pokemon:
    def __init__(self, nickname, type, *moves):
        self._nickname = nickname
        self._type = type
        self._moves = moves
    
    def speak(self):
        return f"My nickname is {self._nickname} and my type is {self._type}."

    def getMoves(self):
        return "My moves are: " + " ".join(self._moves) + "."

pikachu = Pokemon("Pika", "Electric", "Charm", "Growl", "Nasty Plot", "Nuzzle")
print(pikachu.speak())
print(pikachu.getMoves())
