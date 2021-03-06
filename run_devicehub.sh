#!/bin/bash

docker -v

if [ $? != "0" ]
then
	curl -fsSL https://get.docker.com/ | sudo sh
fi

sudo docker stop devicehub_api
sudo docker rm devicehub_api
sudo docker stop ouroboros
sudo docker rm ouroboros

sudo docker run -d --restart always -t --net=host -v /etc/localtime:/etc/localtime:ro -v /var/run/docker.sock:/var/run/docker.sock --name devicehub_api kijen98/devicehub_api:$1 $2

sudo docker run -d --restart always --name ouroboros -v /etc/localtime:/etc/localtime:ro -v /var/run/docker.sock:/var/run/docker.sock pyouroboros/ouroboros -i 30

