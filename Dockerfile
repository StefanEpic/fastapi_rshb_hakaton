FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /game_app

WORKDIR /game_app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

WORKDIR src

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
