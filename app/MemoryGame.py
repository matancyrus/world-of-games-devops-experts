import random
from time import sleep



def get_list_from_user(difficulty):
    while True:
        try:
            numbers = list(map(int, input(
                f"Enter {difficulty} whole numbers separated by spaces: "
            ).split()))
            if len(numbers) == difficulty and all(n >= 0 for n in numbers):
                return numbers
            print("Invalid input. Please try again.")
        except ValueError:
            print("Please enter whole numbers only.")

def memory_game(difficulty=1):
    new_list = []
    for i in range(difficulty):
        num = random.randint(1, 101)
        new_list.append(num)
    print("Please remember the following numbers:\n")
    print(new_list)
    sleep(0.7)
    print("\033[H\033[J", end="")
    user_answer = get_list_from_user(difficulty)
    if user_answer == new_list:
        print("Hurray! You passed!")
        return True
    else:
        print("Oops, wrong answer!")
        return False