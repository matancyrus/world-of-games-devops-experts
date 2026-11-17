from MemoryGame import memory_game
from CurrencyRouletteGame import currency_rolette_game
from GuessGame import guess_game
from Live import greet, load_game
from Score import add_score
from Utils import BAD_RETURN_CODE

def main():
    greet("Matan")
    chosen_game, chosen_difficulty = load_game()
    print(f"You chose game number: {chosen_game}")
    print(f"You chose difficulty level: {chosen_difficulty}")
    #Choose game
    if chosen_game == 1:
        result = memory_game(difficulty=chosen_difficulty)
    if chosen_game == 2:
        result = guess_game(difficulty=chosen_difficulty)
    if chosen_game == 3:
        result = currency_rolette_game(difficulty=chosen_difficulty)
    if result is True:
        score = add_score(chosen_difficulty)
        if score == BAD_RETURN_CODE:
            print("You won, but the score could not be saved.")
        else:
            print(f"Game completed successfully! Total score: {score}")
    else:
        print("Game over!")

if __name__ == "__main__":
    main()