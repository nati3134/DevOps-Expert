import urllib.request as r
import json
import random
import os

def get_money_interval(difficulty):
    # Will get the Current currency
    # and generate an int : difficulty = d, money = t [(t - (5 - d), t + (5 - d))]
    # API key from "free.currencyconverterapi.com": 2e015e19466c486dc19f
    
    difficulty = int(difficulty)
    url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=2e015e19466c486dc19f"
    response = r.urlopen(url)
    data = json.load(response)
    # ex: exchange rate USD ILS (3.24571)
    # usd: Random numbers of US  (12)
    # t: The Value of ILS in USD currency
    ex = int(data["USD_ILS"])
    usd = int(random.uniform(1, 100))
    t = usd * ex 
    low =  int(t - (5 - difficulty))
    high = int(t + (5 - difficulty))
    return usd, t, low, high

def get_guess_from_user(usd):
    # User needs to guess the Value to a given amount of USD
    while True:
        try:
            guess = int(input(f"Guess the value of {usd}$ in ILS: "))
        except ValueError:
            print("Error: Enter just numbers please, not letters, words ,etc...")
            continue
        return guess


def CurrencyRouletteGame(difficulty):
    # Will call all other functions to start the game
    usd, t, low, high = get_money_interval(difficulty)
    guess = get_guess_from_user(usd)
    os.system('cls' if os.name == 'nt' else 'clear')
    if high >= guess >= low:
        print("Wosoome guessing :)")
        return True
    else:
        print("Try again :(")
        return False
