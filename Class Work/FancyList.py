from random import choice 

class FancyList(list):
    def append(self, *items):
        for item in items:
            super().append(item)

    def random_item(self):
        return choice(self)
    
    def __str__(self):
        strings = (str(item) for item in self)
            
        return " ".join(strings)
    

listy = FancyList()
listy.append(1, 2, 3)

print(listy)

# listy.append(2)
# print(listy.random_item())