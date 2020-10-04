from os import system
from CommandLine import CommandLine
from Map import Map

class GameManager:
    def __init__(self):        
        self.map = Map()
  
    def start(self):
        self._play_introduction_dialog()
        
        while(True):
            print("\nIt's your turn")
            print("What do you want to do?")
            print()

            command = input().lower()
            
            system('clear')
            CommandLine.parse(command)

    def _play_introduction_dialog(self):
        system('clear')
        print("Welcome to the dungeon!")
        print("You are tasked with finding the exit and getting out alive.")
        print()
        print("Type 'start' to begin your adventure")
        print("Type 'tutorial' to get a brief introduction")
        print()

        command = input().lower()

        if command == 'tutorial':
            print("Jokes on you, there's no tutorial")
            print("Game starting soon...")
            print("...")
            print("...")
        elif command == 'start':
            print("Fine I will start the game...")
        else:
            print("Not sure what you meant, but game is starting...")
        
        system('clear')
        
GameManager().start()
