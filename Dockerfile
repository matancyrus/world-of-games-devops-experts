FROM python:3-alpine
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app .
COPY app/Scores.txt /Scores.txt
ENV SCORES_FILE_NAME=/Scores.txt
CMD ["python", "MainScores.py"]
