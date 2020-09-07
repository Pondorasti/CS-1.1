from random import randint 
from Ability import Ability

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.abilities = list()
        self.armors = list()

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage = ability.attack()
        
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_defense = 0
        for armor in self.armors:
            total_defense = armor.block()
    
    
    
    def fight(self, opponent):
        if randint(0, 2) == 0:
            print(self.name)
        else:
            print(opponent.name)
    
    


if __name__ == "__main__":
    hero = Hero("Alex", 200)

    debugging_ability = Ability("Debbugging", 20)
    random_ability = Ability("Smarty Pants", 90)
    hero.add_ability(debugging_ability)
    hero.add_ability(random_ability)
    
    print(hero.attack())


