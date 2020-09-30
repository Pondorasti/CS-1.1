from abc import ABC, abstractmethod

class MovableMixin(ABC):
    @abstractmethod
    def move_to(self, x: int, y: int):
        pass