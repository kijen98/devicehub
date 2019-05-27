#!/bin/bash

sudo docker build --force-rm=true --tag kijen98/devicehub_base:latest ./Dockerfiles/base/

sudo docker push kijen98/devicehub_base:latest

