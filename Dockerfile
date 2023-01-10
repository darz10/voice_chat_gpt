from python:3.9.6-buster

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade -r requirements.txt 
COPY . .