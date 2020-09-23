class Sword():
    def __init__(self, name, damage):
        self.damage = damage
        self.name = name
    
    @staticmethod
    def showAbilities():
        print("Swords can only attack orcs and elves, and do zero damage agains magic armour.")


Sword.showAbilities()
