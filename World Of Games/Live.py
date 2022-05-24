from MemoryGame import memory_game
from GuessGame import guess_game 
from CurrencyRouletteGame import CurrencyRouletteGame
from score import add_score

def welcome():
     first_name = input ("Enter your name:")
     print(f"\nhello {first_name} and welcome to the World of Games (WoG). \n Here you can find many cool games to play.")



def load_game():
     print('''
     Please choose a game to play:
     1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
     2. Guess Game - guess a number and see if you chose like the computer
     3. Currency Roulette - try and guess the value of a random amount of USD in ILS
     ''')
     
     while True:
          selected_game = input ("select game:")
          try:
               if int(selected_game) > 3 or int(selected_game) < 1:
                    print ("\nSorry, please enter numbers from 1 - 3.\n")
               else:
                    break     
          except ValueError:
               print ("\nSorry, please enter numbers only.\n")
          continue

         
     while True:
          selected_difficulty = input("Please choose game difficulty from 1 to 5:")
          try:
               if int(selected_difficulty) > 5 or int(selected_difficulty) == 0 :
                    print ("\nSorry, please enter numbers from 1 - 6.\n")
               else:
                    break
          except ValueError:
               print ("\nSorry, please enter numbers only.\n")
          continue
          

     game_map = {'1': memory_game, '2': guess_game, '3': CurrencyRouletteGame }

     res = game_map[selected_game](selected_difficulty)
     if res:
          add_score(selected_difficulty)
     