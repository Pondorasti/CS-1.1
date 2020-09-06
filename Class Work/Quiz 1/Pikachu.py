from Pokemon import Pokemon

class Pikachu(Pokemon):
    def __init__(self, nickname, type, hat, *moves):
        super().__init__(nickname, type, ", ".join(moves))
        self._hat = hat
    
    def speak(self):
        return super().speak() + f"\nI also have a cool hat named: {self._hat}"

pikest = Pikachu("Pika Pika", "Electric", "Top Hat", "Quake", "Nuzzle")

print(pikest.speak())
print(pikest.getMoves())