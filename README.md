Welcome to DeviceHub!
This cooperative IOT development application is very simple to use.

Run below line for download run_devicehub.sh

curl -L -o run_devicehub.sh https://docs.google.com/uc?export=download

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
