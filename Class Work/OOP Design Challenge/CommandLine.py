from abc import ABC

class CommandLine(ABC):

    __commands = {}

    @classmethod
    def parse(cls, input):  
        arguments = input.split(" ")
        if arguments[0] in cls.__commands:
            if len(arguments) < 2:
                print("Show help")
                return 
            
            key = arguments[0]
            option = arguments[1]

            if option.startswith("--", 0, 2):
                for command in cls.__commands[key]:
                    if command['option_name'] == option:
                        command['action']()
                        return 

                print(f"Unknown argument for command '{key}'.")
            elif option.startswith("-", 0, 1):
                for command in cls.__commands[key]:
                    if command['option_name'] == option:
                        command['action']()
                        return
                        
                print(f"Unknown argument for command '{key}'.")
            else:
                print(f"Unknown argument for command '{key}'.")
        else:
            print("Command not found!")
        
        # pass

    @classmethod
    def add_argument(cls, command_name: str, short_option_name: str, option_name: str, help: str, action):
        new_command = {
            'short_option_name': short_option_name,
            'option_name': option_name,
            'help': help,
            'action': action
        }

        for key in cls.__commands:
            if key == command_name:
                cls.__commands[key].append(new_command)
                return 
        
        cls.__commands[command_name] = []
        cls.__commands[command_name].append(new_command)