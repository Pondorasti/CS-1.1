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
        print(self.map)
    

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

GameManager().print_map()

