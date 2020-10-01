from os import system
from CommandLine import CommandLine
from Map import Map

class GameManager:
    def __init__(self):        
        self.map = Map()
        
    def start(self):
        self.play_introduction_dialog()
        
        while(True):
            print("It's your turn")
            print("What do you want to do?")
            print()

            command = input().lower()
            
            system('clear')
            CommandLine.parse(command)

    def play_introduction_dialog(self):
        system('clear')
        print("Welcome to the dungeon!")
        print("You are tasked with finding the exit and getting out alive.")
        print()
        print("Type 'start' to begin your adventure")
        print("Type 'tutorial' to get a brief introduction")
        
        # while(True):
        #     command = input().lower()
        #     CommandLine.parse(command)
            
        #     if command == 'tutorial':
        #         print(command)
        #     elif command == 'start':
        #         print(command)
        #     else:
        #         print("That is not a valid command.")
        
GameManager().start()
