# world-of-games-devops-experts

Three console games (Memory, Guess and Currency Roulette) with persistent scoring and a Flask score service.

## Run locally

Run the game and score service in separate terminals.

```bash
pip install -r app/requirements.txt
python app/MainGame.py
python app/MainScores.py
```

The score is saved in `app/Scores.txt` and displayed at http://localhost:8777. The `SCORES_FILE_NAME` environment variable overrides the file location (Docker uses `/Scores.txt`).

## Docker

```bash
docker compose up --build -d
docker compose down
```

## E2E test

Requires Chrome and Selenium. Stop the Compose service, then run with the isolated test score of 100:

```bash
pip install selenium
docker run --rm -p 8777:8777 \
  -v "$(pwd -P)/tests/Scores.txt:/Scores.txt:ro" \
  matancyrus/world-of-games:latest
```

In another terminal:

```bash
python tests/e2e.py
echo $?
```

Exit code `0` means success; a nonzero code means failure.

.
├── Dockerfile
├── README.md
├── app
│   ├── CurrencyRouletteGame.py
│   ├── GuessGame.py
│   ├── Live.py
│   ├── MainGame.py
│   ├── MainScores.py
│   ├── MemoryGame.py
│   ├── Score.py
│   ├── Scores.txt
│   ├── Utils.py
│   ├── __pycache__
│   │   ├── CurrencyRouletteGame.cpython-314.pyc
│   │   ├── GuessGame.cpython-314.pyc
│   │   ├── MemoryGame.cpython-314.pyc
│   │   ├── Score.cpython-314.pyc
│   │   ├── Utils.cpython-314.pyc
│   │   └── live.cpython-314.pyc
│   └── requirements.txt
├── docker-compose.yml
└── tests
    ├── Scores.txt
    └── e2e.py