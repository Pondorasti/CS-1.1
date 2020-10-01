from Mixins.PlaceableMixin import PlaceableMixin

class Tile(PlaceableMixin):
    def __init__(self, x: int, y: int, shorthand_name: str):
        
        inspect_info = ""
        if shorthand_name == "|" or shorthand_name == "-":
            inspect_info = "It's just a wall"
        else:
            inspect_info = "This looks like a chest"

        super().__init__(x, y, shorthand_name, inspect_info)