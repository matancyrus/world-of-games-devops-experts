import os

SCORES_FILE_NAME = os.getenv("SCORES_FILE_NAME", 
    os.path.join(os.path.dirname(os.path.abspath(__file__)),
    "Scores.txt")
)
BAD_RETURN_CODE = -1  # Indicates failure; valid scores are non-negative.

def Screen_cleaner():
    print("\033[H\033[J", end="")