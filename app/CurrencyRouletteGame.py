import random
import requests
from decimal import Decimal, InvalidOperation

def get_money_interval(difficulty, total):
    difference = 5 - difficulty
    return total - difference, total + difference

def get_guess_from_user(usd_amount):
    while True:
        try:
            guess = Decimal(input(f"How much is ${usd_amount} in ILS? "))
            if guess.is_finite() and guess >= 0:
                return guess.quantize(Decimal("0.01"))
        except InvalidOperation:
            pass
        print("Invalid input! Enter a positive number or zero.")
        
    #Actual game
def currency_rolette_game(difficulty):
    usd_amount = random.randint(1, 100)
    try:
        response = requests.get(
            "https://api.frankfurter.dev/v2/rate/usd/ils",
            timeout=5
        )
        response.raise_for_status()
        rate = Decimal(str(response.json()["rate"]))
        if not rate.is_finite() or rate <= 0:
            raise ValueError("Invalid exchange rate")
    except (requests.RequestException, ValueError,
            KeyError, TypeError, InvalidOperation):
        print("Could not retrieve the exchange rate. Round cancelled.")
        return False
    total = (Decimal(usd_amount) * rate).quantize(Decimal("0.01"))
    lower, upper = get_money_interval(difficulty, total)
    guess = get_guess_from_user(usd_amount)
    if lower <= guess <= upper:
        print("Correct! You win!")
        return True
    print(f"Wrong! The correct amount was {total} ILS.")
    return False
