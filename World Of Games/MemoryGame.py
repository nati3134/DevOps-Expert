import random
from os import system, name
from time import sleep

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def memory_game(level):
    num_list = [str(i) for i in range(1, 101)]
    result = " ".join(random.sample(num_list, int(level)))
    print(result)
    sleep(0.7)
    clear()

    usr_guess = input ("what was the num?: ")

    if usr_guess == result:
        print ("god job!")
    else:
        print ("better luck next time")







