FROM ubuntu:latest
RUN apt -y update && apt -y upgrade && apt install -y python3 python3-pip && pip install flask waitress
COPY . /app
CMD cd /app && flask run
