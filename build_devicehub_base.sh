#!/bin/bash

sudo docker build --force-rm=true --tag kijen98/devicehub_base:$1 ./devicehub_$1/base/

sudo docker push kijen98/devicehub_base:$1

