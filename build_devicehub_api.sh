#!/bin/bash

sudo docker build --force-rm=true --tag kijen98/devicehub_api:$1 ./devicehub_$1/api/

sudo docker push kijen98/devicehub_api:$1

