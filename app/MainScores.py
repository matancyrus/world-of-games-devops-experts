from flask import Flask
from Utils import SCORES_FILE_NAME

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME) as file:   
            score = int(file.read()) 
            if score < 0:
                raise ValueError("Score cannot be negative")
            return f"""<html>
        <head><title>Scores Game</title></head>
        <body>
            <h1>The score is <span id="score">{score}</span></h1>
        </body>
        </html>
        """
    except:
        return '<h1 id="score" style="color:red;">Invalid score</h1>', 500
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8777, debug=True)