from abc import ABC, abstractmethod

class PlaceableMixin():
    def __init__(self, x: int, y: int, shorthand_name: chr, inspect_info: str):
        self._x = x
        self._y = y

        self._shorthand_name = shorthand_name
        self._inspect_info = inspect_info
    
    def inspect(self):
        print(self._inspect_info)
    
    def get_short_name(self):
        return self._shorthand_name
