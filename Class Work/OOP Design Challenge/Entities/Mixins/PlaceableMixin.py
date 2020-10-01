from abc import ABC, abstractmethod

class PlaceableMixin():
    def __init__(self, x: int, y: int, inspect_info: str):
        self._x = x
        self._y = y

        self._inspect_info = inspect_info
    
    def inspect(self):
        print(self._inspect_info)
