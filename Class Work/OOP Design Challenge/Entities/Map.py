from random import randint
from Hero import Hero
from Monster import Monster
from Tile import Tile
from CommandLine import CommandLine
from os import system

class Map:
    def __init__(self):
        map_number = randint(1, 3)
        file = open(f"map{map_number}.txt", "r")
        
        rows = 0
        map = []
        for line in file:
            map.append([])
            columns = 0
            for cell in line:
                if cell == '0':
                    map[rows].append(Tile(rows, columns, "0"))
                elif cell == 'H':
                    self._hero = Hero(rows, columns)
                    CommandLine.add_argument("move", "-n", "--north", "Moves your character forward", self.move_forward_hero)
                    CommandLine.add_argument("move", "-s", "--south", "Moves your character backward", self.move_backward_hero)
                    CommandLine.add_argument("move", "-w", "--west", "Moves your character left", self.move_left_hero)
                    CommandLine.add_argument("move", "-e", "--est", "Moves your character right", self.move_right_hero)
                    map[rows].append(self._hero)
                elif cell == 'M':
                    map[rows].append(Monster(rows, columns))
                elif cell == 'D':
                    map[rows].append(Tile(rows, columns, "D"))
                elif cell == 'C':
                    map[rows].append(Tile(rows, columns, "C"))
                elif cell != "\n":
                    map[rows].append(Tile(rows, columns, cell))
                
                columns += 1
            rows += 1

        file.close()
        self.number_of_rows = rows
        self.number_of_columns = len(map[0])
        self.map = map

    def print_map(self):
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                print(f"{self.map[row][column].get_short_name()}", end="")
            print()

    def move_forward_hero(self):
        nextX = self._hero._x - 1
        nextY = self._hero._y 
        self.move_hero(nextX, nextY, self._hero._x, self._hero._y)

    def move_backward_hero(self):
        nextX = self._hero._x + 1
        nextY = self._hero._y 
        self.move_hero(nextX, nextY, self._hero._x, self._hero._y)

    def move_left_hero(self):
        nextX = self._hero._x 
        nextY = self._hero._y - 1
        self.move_hero(nextX, nextY, self._hero._x, self._hero._y)
    
    def move_right_hero(self):
        nextX = self._hero._x 
        nextY = self._hero._y + 1
        self.move_hero(nextX, nextY, self._hero._x, self._hero._y)
        
    def move_hero(self, nextX, nextY, x, y):
        if self.is_tile_free(nextX, nextY):
            self._hero.move_to(nextX, nextY)
            self.map[nextX][nextY] = Hero(nextX, nextY)
            self.map[x][y] = Tile(nextX, nextY, "0")
            self.print_map()
        else:
            self.print_map()
            print("You can only move on empty tiles.")
    
    def is_tile_free(self, x: int, y: int):
        if self.map[x][y]._shorthand_name == '0':
            return True
        return False

# Map().print_map()