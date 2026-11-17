from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

def add_score(difficulty):
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
            if current_score < 0:
                raise ValueError("Score cannot be negative")
    except FileNotFoundError:
        current_score = 0
    except ValueError:
        print("Invalid score file")
        return BAD_RETURN_CODE
    except OSError:
        print("Failed to read score")
        return BAD_RETURN_CODE
    POINTS_OF_WINNING = (difficulty * 3 ) + 5
    new_score = current_score + POINTS_OF_WINNING
    try:
        with open(SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))
    except OSError:
        print("Failed to save score")
        return BAD_RETURN_CODE
    return new_score