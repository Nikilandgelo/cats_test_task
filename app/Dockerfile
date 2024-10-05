FROM python:3.12-alpine
WORKDIR /app

COPY requirements.txt .
RUN apk add postgresql-dev & pip install -r requirements.txt

COPY . .

ENTRYPOINT python3 manage.py makemigrations && python3 manage.py migrate \
           && python3 manage.py runserver 0.0.0.0:8000
EXPOSE 8000