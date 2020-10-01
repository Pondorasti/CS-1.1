from Entity import Entity

class Hero(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(40, 7, 3, 1, 3, "H")
        self._x = x
        self._y = y


# alex = Hero(0, 0)
# tristan = Hero(0, 0)
# brian = Hero(0, 0)
# alex.attack(tristan)