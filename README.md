Welcome to DeviceHub!
This cooperative IOT development application is very simple to use.

Let's Download run_devicehub.sh


wget --load-cookies cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1GzxiJO-2x_hMM9F3bgk7U-L9bNBO-Yai' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1GzxiJO-2x_hMM9F3bgk7U-L9bNBO-Yai" -O run_devicehub.sh


And execute this line for setting permission.


chmod +x run_devicehub.sh


Just execute sudo ./run_devicehub.sh (your architecture) (your projectID) in your device.
For example, your Raspberry pi is armv7l architecture for Myproject0105,
./run_devicehub.sh armv7l Myproject0105

And install DeviceHub application in your android smartphone.

Make your project and register your device by its IP address that is internel IP.

If you register docker image image:tag on your device, it will be ran on your device soon.
You can also register docker run option, too.

If you want to register device for another projectID, just input same execution for that ID.

If you want to stop Devicehub, than just execute ./stop_devicehub.sh that can be downloade by execute below line.

wget --load-cookies cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1rNRIfMS0ct0x3PTkzrmscit0mAesXY8u' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1rNRIfMS0ct0x3PTkzrmscit0mAesXY8u" -O stop_devicehub.sh

Feel Fun!


[How to Check your Devicehub_api logs]

sudo docker logs devicehub_api


[Example of Executing images]

Image1)

Name: kijen98/mysql:x86_64

Option: --net=host -p 3306:3306 -e MYSQL_ROOT_PASSWORD=examplepassword


Image2)

Name: kijen98/wordpress:x86_64

Option: --net=host -p 80:80
