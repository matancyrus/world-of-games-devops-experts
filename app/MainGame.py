from MemoryGame import memory_game
from CurrencyRouletteGame import currency_rolette_game
from GuessGame import guess_game
from Live import greet, load_game

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
    if result:
        print("Game completed successfully!")
    else:
        print("Game over!")

if __name__ == "__main__":
    main()