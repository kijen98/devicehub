Welcome to DeviceHub!
This cooperative IOT development application is very simple to use.

Let's make run_devicehub.sh

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

sudo docker run -d --restart always -t --net=host -v /var/run/docker.sock:/var/run/docker.sock --name devicehub_api kijen98/devicehub_api:$1 $2

sudo docker run -d --restart always --name ouroboros -v /var/run/docker.sock:/var/run/docker.sock pyouroboros/ouroboros -i 30


And execute this line for setting permission.

chmod +x run_devicehub.sh

Just execute ./run_devicehub.sh (your architecture) (your projectID) in your device.
For example, your Raspberry pi is armv7l architecture for Myproject0105,
./run_devicehub.sh armv7l Myproject0105

And install DeviceHub application in your android smartphone.

Make your project and register your device by its IP address that is internel IP.

If you register docker image image:tag on your device, it will be ran on your device soon.
You can also register docker run option, too.

If you want to register device for another projectID, just input same execution for that ID.

If you want to stop Devicehub, than just execute ./stop_devicehub.sh

Feel Fun!
