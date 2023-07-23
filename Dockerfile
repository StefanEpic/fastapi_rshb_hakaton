FROM python:3.10-alpine

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

WORKDIR game_app

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
