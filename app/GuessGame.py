import random

def generate_number(difficulty:int) -> int:
    secret_numnber = random.randint(1, difficulty)
    return secret_numnber

 
def guess_game(difficulty):
    print("Welcome to the Guessing Game!")
    while True:
        try:
            get_guess_from_user = input(f"Please enter a number between 1 and {difficulty}:\n")
            secret_num = generate_number(difficulty)
            if int(get_guess_from_user) == secret_num:
                print(f"Hurray, The correct number is {secret_num}")
                return True
            elif (1 > int(get_guess_from_user)) or (int(get_guess_from_user) > difficulty):
                print("invalid range, enter a number within the expected range")
            else: 
                print("Oops, try again!")
                continue
        except ValueError:
            print(f"Please enter a number from 1 and {difficulty}")
            continue
