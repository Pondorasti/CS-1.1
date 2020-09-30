from abc import ABC, abstractmethod

class PlaceableMixin():
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y