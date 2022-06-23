FROM ubuntu

RUN apt update && apt -y upgrade
RUN apt install -y python3 python3-pip
RUN pip install flask waitress

RUN mkdir /root/server

COPY . /root/server

CMD ["python3","/root/server/main.py"]

EXPOSE 80
