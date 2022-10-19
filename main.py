import random, os, time

print("Welcome to Rock, Paper, Scissors!\n")


#-----------------------------
#Initialize variables
#-----------------------------
choices = ["Rock", "Paper", "Scissors"]
games_played = 0
games_won = 0
games_lost = 0
#-----------------------------


#-----------------------------
#Define functions for our code
#-----------------------------
def clear_screen():
  os.system("clear")

def win():
  global games_won
  games_won +=1

def loss():
  global games_lost
  games_lost +=1

def scoreboard():
  global games_played
  global games_won
  global games_lost
  
  games_played +=1
  print("SCOREBOARD")
  print(f"- Games Played: {games_played}")
  print(f"- Games Won: {games_won}")
  print(f"- Games Lost: {games_lost}")
  print(f"- Win %: {games_won/games_played*100}")
  print()
  input("Press enter to continue.")
  clear_screen()

def get_user_choice():
  print("Type Rock, Paper, or Scissors.\n")
  user_choice = input("->").title().strip()
  print()
  return user_choice

def get_computer_choice():
  #Version 1
  index_number = random.randint(0,2)
  comp_choice = choices[index_number]
  print(comp_choice)
  
  #Version 2
  #comp_choice = random.choice(choices)
  return comp_choice

def show_choices(user_choice, comp_choice):
  counter = 0
  clear_screen()
  print("Rock!")
  time.sleep(1.5)
  print("Paper!")
  time.sleep(1.5)
  print("Scissors!")
  time.sleep(1.5)
  while counter < 3:
    counter +=1
    print("Shoot!")
    time.sleep(.75)
  clear_screen()
  print(f"You chose: {user_choice}. The computer chose: {comp_choice}.")
  print()

def game_loop():
  while True:
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    show_choices(user_choice, comp_choice)
    
    #Check for a tie
    if user_choice == comp_choice:
      print("You tied.")
      print()
      scoreboard()
      
    #Check for a loss
    elif (user_choice == "Rock" and comp_choice == "Paper") or (user_choice == "Paper" and comp_choice == "Scissors") or (user_choice == "Scissors" and comp_choice == "Rock"):
      print("You lost.")
      print()
      loss()
      scoreboard()
  
    #Check for a win
    elif  (user_choice == "Rock" and comp_choice == "Scissors") or (user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Scissors" and comp_choice == "Paper"):
      print("You won!")
      print()
      win()
      scoreboard()
  
    #Something went wrong
    else:
      print("An error occurred.")
      break
#-----------------------------

      
#-----------------------------
#Here is what runs our entire code
#-----------------------------
game_loop()