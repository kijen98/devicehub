import sys
import os
import socket
import time
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

def getdeviceip():
    #get device ip address by socket return
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    time.sleep(0.01)
    return ip

ip_address_dot = getdeviceip().split('.')
ip_address = ''
for i in range(len(ip_address_dot) - 1):
    ip_address = ip_address + ip_address_dot[i] + '-'
ip_address = ip_address + ip_address_dot[len(ip_address_dot) - 1]

if len(sys.argv) == 1:
    print("No projectID, Please input project ID")
    exit(1)
projectID = sys.argv[1]

cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://devicehub-e7c8d.firebaseio.com/'
})

projectref = 'projects/' + projectID
#deviceref = projectref + '/device/' + ip_address
deviceref = projectref + '/device/' + '192-168-00-01'
imageref = deviceref + '/image'
ref = db.reference(imageref)

dict = ref.get()

image_name = []
run_option = []
for key in dict.keys():
    image_name.append(dict[key]['name'])
    run_option.append(dict[key]['option'])

container_name = []
print("Executing Image List")
for i in range(len(image_name)):
    container_name.append("container_"+str(i))
    print(image_name[i] + ' ' + run_option[i])

os.system("sudo docker stop $(sudo docker ps -a | grep -i \"container\"| awk 'NR>1 {print $1}') && sudo docker rm $(sudo docker ps -a | grep -i \"container\"| awk 'NR>1 {print $1}') || true")

for i in range(len(container_name)):
    command = "sudo docker run -d "+run_option[i]+" --name "+container_name[i]+" "+image_name[i]
    os.system(command)

os.system("sudo docker stop devicehub_api")
