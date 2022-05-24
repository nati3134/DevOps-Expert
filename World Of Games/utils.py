from os import system, name


SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')