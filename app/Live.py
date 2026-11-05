#Greets the player
def greet(playername:str) -> None:
    if not isinstance(playername, str):
        raise TypeError("This function accepts strings only!")
    print(f"Hello {playername} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")

#Loads the game
def load_game():
    #Choose game
    while True:
        try:
            num = int(input("""
Please choose a game to play:
1. Memory Game
2. Guess Game
3. Currency Roulette\n
"""))
            if num in [1,2,3]:
                break
            print("You must choose a number between 1-3.")
            continue
        #Validation
        except ValueError:
            print("You must enter a number and not a letter")
            continue
    while True:
        try:
            #Choose difficulty
            difficulty = int(input("""\nPlease choose game difficulty from 1 to 5:\n
"""))
            if difficulty in [1,2,3,4,5]:
                break
            print("You must choose a number between 1-3.")
            continue
        #Validation
        except ValueError:
            print("You must enter a number and not a letter")
            continue
    return int(num), int(difficulty)
    