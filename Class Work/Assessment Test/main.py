#Welcome to Monster Dance Battle!
from random import choice

#npc means non-playable character, this will be the monster your player monster will be battling
#hp means hit points or how much overall health a monster has
#dance moves from an opposing monster will reduce hit points by the dance score amount

#TODO ✅: write a function that will read the contents of a file containing monster npc info and return a dictionary of that info
#npc_monsters.txt has the format the info will be in
#hint: be sure to convert the hp numbers to ints!
#Example output {Cookie:20, Kelpie:25, Griffin:30}
def get_npc_monster_dictionary(filename):
  file = open(filename, "r")
  monsters = {}

  for line in file:
    separator_index = line.index(",")
    name = line[:separator_index]
    hp = int(line[separator_index + 1:])

    monsters[name] = hp
    
  file.close()

  return monsters


npc_monster_hps = get_npc_monster_dictionary("Class Work/Assessment Test/npc_monsters.txt")

npc_monster_dance_moves = [
  {"Vogue": 3, "The Moonwalk": 12},
  {"The Twist": 5, "Sprinkler": 10},
  {"Box Step": 4, "Floss": 12}
]

#TODO ✅: Write a function that will randomly select a monster&hp from the given dictionary stored in the npc_monster_hps global variable

#This function will return a tuple, the monster name and hp as one tuple
#Example output: (Cookie, 20)

def select_npc_monster():
  tuples = list(npc_monster_hps.items())
  return choice(tuples)
  


#TODO ✅: Write a function that will randomly select a dance move set with attack values from the given list stored in the npc_monster_dance_moves global variable

#This function will return a dictionary,the dance moves as the dictionary
#Example output: {"Vogue":3, "The Moonwalk":12}
def select_npc_dance_moves():
  return choice(npc_monster_dance_moves)

#TODO ✅: Write a function that will get the monster name and hp from user input. You will need to limit the user entered hp value to be greater than 1 and less than or equal to 30. Keep prompting until the user enters a number that works.

#This function will return a tuple, the monster name and hp as one tuple
#Example output: (Jess, 20)
def build_player_monster():
  print("Hey there!")
  monster_name = input("Choose a name for your monster: ")

  monster_hp = None
  while monster_hp is None:
    tentative_hp = int(input("How many hitpoints do you want: "))
    
    if 1 <= tentative_hp and tentative_hp <= 30:
      monster_hp = tentative_hp
      print("Monster created! \n")
    elif 1 > tentative_hp:
      print("Huh? Are you joking around? You should know that you can't have less than 1 hp!")
    else:
      print("Nice try! Overpowered monsters are not allowed here! Choose a value that is less than or equal to 30.")

  return (monster_name, monster_hp)

#TODO ✅: Write a function that will create the player monster dance moves from user input. You will need to limit the dance move score to be greater than 1 less than or equal to 15. Keep prompting until the user enters a number that works.

#This function will return a dictionary, the dance moves as a dictionary with two dance moves and scores
#get the dance move name as the key
#get the dance move score as the value 
#Example output: {"Sprinkler":3, "Lawnmower":12}
def build_player_monster_dance_moves():
  dance_moves = {}

  for index in range(2):
    move_name = input("Choose a name for dance move %s: " % (index + 1))
    
    move_score = None
    while move_score is None:
      tentative_score = int(input("How cool is your dance move on a scale from 1 to 15: "))

      if 1 <= tentative_score and tentative_score <= 15:
        move_score = tentative_score
        print("Dance move %s created! \n" % (index + 1))
      else:
        print("Your dance move coolness does not meet the competition rules!")

    dance_moves[move_name] = move_score

  print("Finished creating your dance skillset. \n")

  return dance_moves


#TODO ✅: return the player name and the new hp as a tuple and the npc player name and the new hp as a tuple
#Example Output: ("Jess", 20), ("Cookie", 30)
def battle(player_monster, player_dance_moves, npc_monster, npc_dance_moves):
  #TODO ✅: randomly select a npc dance move and display it to the player
  npc_dance_move = choice(list(npc_dance_moves.items()))
  print("Your opponent picked %s" % npc_dance_move[0])

  #TODO ✅: let the user select one of their dance moves from their dance move dictionary
  #keep prompting if they don't enter a valid dance move name
  player_dance_move = None
  player_dance_move_names = player_dance_moves.keys()
  while player_dance_move is None:
    tentative_name = input("Now it's your turn to pick a dance move (Options: %s): " % (", ".join(list(player_dance_move_names))))

    for name in player_dance_move_names:
      if name.lower() == tentative_name.lower():
        player_dance_move = (name, player_dance_moves[name])
        break

    if player_dance_move is None:
      print("This is not a valid dance move name!")

  #TODO ✅: subtract the player dance move score from the npc hp and the npc dance move score from the player hp
  print("Players start dancing! \n")
  new_player_hp = player_monster[1] - npc_dance_move[1]
  new_monster_hp = npc_monster[1] - player_dance_move[1]

  #TODO ✅: show the current hps for both the player and the npc monster
  print("Dance round finished!")
  print("Your hp is %s." % (new_player_hp))
  print("Your opponent's hp is %s. \n" % (new_monster_hp))

  #TODO ✅: return the player name and the new hp as a tuple and the npc player name and the new hp as a tuple
  #hint remember tuples are immutable
  #hint you can return multiple values in Python by separating them by a comma after the return keyword
  return (player_monster[0], new_player_hp), (npc_monster[0], new_monster_hp)
  

#TODO ✅: Finish this function that will use a loop to run the game
#this function doesn't return anything
def run_dance_battle():
  #TODO ✅: call the build_player_monster() function and store the result in a variable
  player_monster = build_player_monster()

  #TODO ✅: call the build_player_monster_dance_moves() function and store the result in a variable
  player_dance_moves = build_player_monster_dance_moves()

  #TODO ✅: call the select_npc_monster() function and store the result in a variable
  npc_monster = select_npc_monster()

  #TODO ✅: call the select_npc_dance_moves() function and store the result in a variable
  npc_dance_moves = select_npc_dance_moves()

  #TODO ✅: finish this while loop condition to keep taking turns until either the npc or the player is at 0
  print("Let the game begin! \n")
  round_count = 1
  while player_monster[1] > 0 and npc_monster[1] > 0:
    print("Round %s" % (round_count))
    round_count += 1

    player_monster, npc_monster = battle(
      player_monster, player_dance_moves,
      npc_monster, npc_dance_moves
    )

  #TODO ✅: use a conditional statement to print who won!
  if player_monster[1] <= 0 and npc_monster[1] <= 0:
    print("Stalemate! We dont have a winner today :/")
  elif player_monster[1] <= 0:
    print("You lost! Better luck next time!")
  elif npc_monster[1] <= 0:
    print("Congratulation! You are a true hero!")



#TODO ✅: write two simple automated tests to test the functions you wrote

assert(npc_monster_hps.get(select_npc_monster()[0]) is not None)
assert(select_npc_dance_moves() in npc_monster_dance_moves)
assert(type(list(get_npc_monster_dictionary("Class Work/Assessment Test/npc_monsters.txt").values())[0]) is int)


run_dance_battle()

#------------------------------------------------------

#Part 2: Skip this if you aren't comfortable with Object Oriented Programming 

#The code you wrote above as seprate functions and information stored in tuples and dictionaries works but it isn't as readable and resuable as it would be if we thought of the monsters and npc monsters as objects. For Part 2 your task is to make this project more object oriented! One way to approach this would be to make a Monster class so that both the npc and player monster information could be represented as Monster objects.

#1. To complete this part of the project first complete the Monster class and replace all the monster and npc monster code to work with Monster objects.

#2. Complete the UltraMonster.py class which will inherit from Monster.py. UltraMonster.py will add a new property called "defense_score" which will be an integer. Ultra monster will override the subtract_hp() method inherited from Monster to reduce the effect of a dance move by adding the defense_score to the monster's hp. 

#3. Bonus (optional): make your monster randomly be able to turn into an ultra monster while the game is running

#4. Stretch (optional): Feel free to make the game even cooler! Some ideas are to add items to the Monsters or create several different types of monsters using inheritance and classes. You could also use pygame or turtle graphics to add graphics to your game!

