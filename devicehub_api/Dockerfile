FROM kijen98/devicehub_base:latest

RUN apt-get update
RUN apt-get install curl -y
RUN curl -fsSL https://get.docker.com/ | sudo sh

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app/

ENTRYPOINT ["python", "devicehub_api.py"]

