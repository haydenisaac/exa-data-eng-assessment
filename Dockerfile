FROM ubuntu:latest

COPY . /opt/app
WORKDIR /opt/app

RUN apt-get update && apt install -y python3 pip vim
RUN pip install -r requirements.txt


