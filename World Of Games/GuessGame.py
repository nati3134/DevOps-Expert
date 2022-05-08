import random


def guess_game(difficulty):
    lower = 1

    higher = int(difficulty) * 3

    random_number = (random.randint(lower, higher))

    print(f"guess number range between {lower} - {higher}.")

    while True:
       
       try:
           user_guess = int(input("pls guess a number: "))
           break
       except ValueError:
               print ("\nSorry, please enter numbers only.\n")
       continue
    
    if user_guess == random_number:
        print ("good job!")
    else:
        print ("better luck next time")

