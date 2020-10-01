from Mixins.PlaceableMixin import PlaceableMixin

class Tile(PlaceableMixin):
    def __init__(self, x: int, y: int, shorthand_name: str):
        
        inspect_info = ""
        if shorthand_name == "C":
            inspect_info = "This looks like a chest"
        elif shorthand_name == "0":
            inspect_info = "There's nothing here, just an empty tile"
        else:
            inspect_info = "It's just a wall"

        super().__init__(x, y, shorthand_name, inspect_info)