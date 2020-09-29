from abc import ABC, abstractmethod
from random import randint
from Dice import Dice

class Entity(ABC):
    @abstractmethod
    def __init__(self, hp: int, attack_rng: int, defense_rng: int, damage: int, armor: int, shorthand_name: chr):
        self._hp = hp
        self._attack_rng = attack_rng
        self._defense_rng = defense_rng
        self._damage = damage
        self._armor = armor
        self._shorthand_name = shorthand_name
        
    
    def defend(self, damage_to_take: int):
        rng = Dice.roll()

        if rng < self._defense_rng:
            print("Clumsy attack! You miss!")
        elif rng < self._defense_rng:
            print("Opponent blocks your attack")
        else:
            damage_taken = self._armor - damage_to_take
            if damage_taken <= 0:
                print("Attack hits, but it cannot go through the armor")
            else:
                print(f"Attack hits, and you manage to do some damage: {damage_taken}")
                self._hp -= damage_taken
                # TODO: Check if dead
    
    @property
    def isDead(self):
        if self._hp < 1 :
            print("Bu dead")
            return True
        else:
            return False

    
# Game Rules

# Each entity has a total of 10 Ability points
# They can be distributed in any way between *attack_rng* and *defense_rng*
# As long as none of the properties are equal to zero

# Attacking
# Whenever an entity attacks they roll their *attack_rng* using 2 10Ds
# If the *attack_rng* is smaller than the *armor* of the entity you attacked, it is a miss
# Otherwise, 
# Note: If *attack_rng* is equal to ... than it means a critical hit and you do twice the damage