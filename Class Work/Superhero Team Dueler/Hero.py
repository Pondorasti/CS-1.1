from random import randint
from Ability import Ability
from Weapon import Weapon
from Armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.abilities = list()
        self.armors = list()

        self.deaths = 1
        self.kills = 0

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

        return total_defense
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def take_damage(self, damage):
        final_damage = damage - self.defend()
        if final_damage > 0:
            self.current_health -= final_damage

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        # Check if any of the Heroes can do damage
        if self.abilities.count == 0 and opponent.abilities.count == 0:
            print("Stalemate")
            return

        # There's also the edge case where abilities do 0 damaga

        # Fight until somebody dies
        while self.is_alive() and opponent.is_alive():
            my_damage = self.attack()
            opponent.take_damage(my_damage)

            opponent_damage = opponent.attack()
            self.take_damage(opponent_damage)

        # Check who is still alive
        if not self.is_alive() and not opponent.is_alive():
            self.add_deaths()
            opponent.add_deaths()

            print("Stalemate")
        elif not self.is_alive():
            self.add_deaths()
            opponent.add_kills()

            print(f"{opponent.name} is a true Hero")
        elif not opponent.is_alive():
            self.add_kills()
            opponent.add_deaths()

            print(f"{self.name} is a true Hero")
        else:
            raise ValueError("Impossible State")

    def add_kills(self, num_kills = 1):
        self.kills += num_kills
    
    def add_deaths(self, num_deaths = 1):
        self.deaths += num_deaths

if __name__ == "__main__":
    # hero = Hero("Alex", 200)

    # debugging_ability = Ability("Debbugging", 20)
    # random_ability = Ability("Smarty Pants", 90)
    # hero.add_ability(debugging_ability)
    # hero.add_ability(random_ability)

    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)

    # hero.take_damage(50)
    # print(hero.current_health)

    # hero.take_damage(5000)
    # print(hero.is_alive())

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
