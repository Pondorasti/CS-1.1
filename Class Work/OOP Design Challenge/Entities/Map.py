from random import randint
from Hero import Hero
from Monster import Monster

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
                    map[rows].append('0')
                elif cell == 'H':
                    map[rows].append(Hero(rows, columns))
                elif cell == 'M':
                    map[rows].append(Monster(rows, columns))
                elif cell == 'D':
                    map[rows].append('D')
                elif cell == 'C':
                    map[rows].append('C')
                elif cell == '|':
                    map[rows].append('|')
                elif cell == '-':
                    map[rows].append('-')
                
                columns += 1

            rows += 1
        
        file.close()
        self.number_of_rows = rows
        self.number_of_columns = len(map[0])
        self.map = map

    def print_map(self):
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                print(f"{self.map[row][column]}", end="")
            print()

Map().print_map()