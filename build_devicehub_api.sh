#!/bin/bash

sudo docker build --force-rm=true --tag kijen98/devicehub_api:latest ./devicehub_api/

sudo docker push kijen98/devicehub_api:latest

