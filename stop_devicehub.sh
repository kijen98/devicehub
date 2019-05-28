#!/bin/bash

sudo docker stop devicehub_api
sudo docker rm devicehub_api
sudo docker stop ouroboros
sudo docker rm ouroboros

sudo docker stop container_0 $(sudo docker ps -a | grep -i "container"| awk 'NR>1 {print $1}')
sudo docker rm container_0 $(sudo docker ps -a | grep -i "container"| awk 'NR>1 {print $1}')
