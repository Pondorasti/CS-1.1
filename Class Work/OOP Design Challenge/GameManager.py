from os import system

class GameManager:
    def __init__(self):
        map = []
        self.length = range(5)

        for i in self.length:
            map.append([])
            for j in self.length:
                map[i].append(0)
        
        self.map = map
        
    def start(self):
        self.play_introduction_dialog()

    def play_introduction_dialog(self):
        system('clear')
        print("Welcome to the dungeon!")
        print("You are tasked with finding the exit and getting out alive.")
        print()
        print("Type 'start' to begin your adventure")
        print("Type 'tutorial' to get a brief introduction")

        
        while(True):
            command = input().lower()
            
            if command == 'tutorial':
                print(command)
            elif command == 'start':
                print(command)
            else:
                print("That is not a valid command.")
        

    def print_map(self):
        def print_pipes():
            for _ in self.length:
                print("-", end="-")
            print("-")
        
        def print_row(line: int):

            for column in self.length:
                print(f"|{self.map[line][column]}", end="")
            print("|")

        for row in self.length:
            print_pipes()
            print_row(row)
        print_pipes()

# GameManager().start()
GameManager().print_map()


# -----------
# |0|0|0|0|0|
# -----------
# |0|0|0|0|0|
# -----------
# |0|0|0|0|0|
# -----------
# |0|0|0|0|0|
# -----------
# |0|0|0|0|0|
# -----------

# D0000
# 00000
# 0M0M0
# 00000
# 00H00
# C0000


# -------------
# | 0 0 0 0 0 |
# |------ 0 0 |
# | 0 M | M 0 |
# | 0 0 | 0 0 |
# | 0 0 H 0 0 |
# -------------
