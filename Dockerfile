FROM python:3.11.9-slim-buster

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
