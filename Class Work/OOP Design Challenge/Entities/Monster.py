from Entity import Entity
from random import randint, choice

class Monster(Entity):
    def __init__(self, x: int, y: int):
        attack_rng = randint(1, 5)
        defense_rng = 5 - attack_rng

        damage = randint(1, 3)
        armor = randint(1, 3)

        super().__init__(40, attack_rng, defense_rng, damage, armor, "M")
        
        self._x = x
        self._y = y

        info_options = [
            ("Chester", "It looks similar to an old chest, but you have an odd feeling about it."),
            ("Samurai", "You see somebody with a serious look.")
        ]

        random_info = choice(info_options)
        self._inspect_info = random_info[2]
