from random import choice

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
    
    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def remove_hero(self, name):
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
                # break
        
        if not found_hero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    
    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths: {kd}")
    
    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.health = health
    
    def attack(self, other_team):
        living_heroes = [hero for hero in self.heroes]
        living_oponents = [hero for hero in other_team.heroes]

        while len(living_heroes) > 0 and len(living_oponents) > 0:
            current_hero = choice(living_heroes)
            current_opponent = choice(living_oponents)

            current_hero.fight(current_opponent)

            if not current_hero.is_alive():
                living_heroes.remove(current_hero)
            if not current_opponent.is_alive():
                living_oponents.remove(current_opponent)

