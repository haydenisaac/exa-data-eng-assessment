FROM ubuntu:latest

COPY ./app /opt/app
COPY ./data /opt/app/data
WORKDIR /opt/app

RUN apt-get update && apt install -y python3 pip vim
RUN pip install -r requirements.txt


