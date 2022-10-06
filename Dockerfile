FROM ubuntu:20.04
RUN apt -y update && apt -y upgrade && apt install -y python3 python3-pip && pip install flask waitress
USER root
COPY . /app
CMD cd /app && flask run
