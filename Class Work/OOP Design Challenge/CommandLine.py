from abc import ABC

class CommandLine(ABC):

    __commands = {}

    @classmethod
    def parse(cls, input):  
        if input == "help":
            print("\nHere's a list of possible commands:\n")
            for key in cls.__commands:
                print(key)
            return 

        arguments = input.split(" ")
        if arguments[0] in cls.__commands: # Check if command exists
            key = arguments[0]
            if len(arguments) < 2: # Show help if there's no options
                cls.show_help(key)
                return 
            
            option = arguments[1]
            if option.startswith("--", 0, 2): # Check for 'option_name'
                for command in cls.__commands[key]:
                    if command['option_name'] == option:
                        command['action']()
                        return 
                
                if option == "--help":
                    cls.show_help(key)
                else:
                    print(f"Unknown argument for command '{key}'.")
            elif option.startswith("-", 0, 1): # Check for 'short_option_name'
                for command in cls.__commands[key]:
                    if command['short_option_name'] == option:
                        command['action']()
                        return
                        
                if option == "-h":
                    cls.show_help(key)
                else:
                    print(f"Unknown argument for command '{key}'.")
            else:
                print(f"Unknown argument for command '{key}'.")
        else:
            print("Command not found!")

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

    @classmethod
    def show_short_help(cls, key):
        print(f"\nusage: {key}", end = " ")
        for command in cls.__commands[key]:
            print(f"[{command['short_option_name']} | {command['option_name']}]", end = " ")
        print()
    
    @classmethod 
    def show_help(cls, key):
        print("\nHere's a list of possible commands:\n")
        for command in cls.__commands[key]:
            print(f"[{command['short_option_name']} | {command['option_name']}]        {command['help']}")
        print()



# Janky Unit Testing

# def hello():
#     print("Hello dear friend")

# def random_int():
#     print(5)

# def stop():
#     print("I don't want this to end!")

# CommandLine.add_argument("say", "-h", "--hello", "Say hello to your friend", hello)
# CommandLine.add_argument("say", "-r", "--random", "Returns a random integer", random_int)
# CommandLine.add_argument("kill", "-m", "--me", "Stops executions of the program", stop)


# while(True):
#     command = input()
#     CommandLine.parse(command)