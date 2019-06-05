import sys
import os
import socket
import time
import copy
import threading
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

class AsyncTask:
    def __init__(self, deviceref):
        self.image_name = []
        self.run_option = []
        self.old_image_name = []
        self.old_run_option = []
        self.deviceref = deviceref

    def get_config(self):
        det_change = 0

        imageref = self.deviceref + '/image'
        ref = db.reference(imageref)
        dict = ref.get()
        if(dict == None):
            return det_change

        self.image_name = []
        self.run_option = []

        for key in dict.keys():
            if len(dict[key].keys()) == 2:
                self.image_name.append(dict[key]['name'])
                self.run_option.append(dict[key]['option'])
            else:
                self.image_name.append("")
                self.run_option.append("")

        if len(self.image_name) != len(self.old_image_name):
            det_change = 1
        else:
            for i in range(len(self.image_name)):
                if (self.image_name[i] != self.old_image_name[i]) or (self.run_option[i] != self.old_run_option[i]):
                    det_change = 1
                    break

        return det_change

    def change_by_config(self):
        print("Executing Configuration is changed")
        self.old_image_name = copy.deepcopy(self.image_name)
        self.old_run_option = copy.deepcopy(self.run_option)

        container_name = []
        print("Executing Image List")
        for i in range(len(self.image_name)):
            container_name.append("container_" + str(i))
            print(self.image_name[i] + ' ' + self.run_option[i])

        os.system("sudo docker stop container_0 $(sudo docker ps -a | grep -i \"container\"| awk 'NR>1 {print $1}')")
        os.system("sudo docker rm container_0 $(sudo docker ps -a | grep -i \"container\"| awk 'NR>1 {print $1}')")

        for i in range(len(container_name)):
            command = "sudo docker run -d " + self.run_option[i] + " --name " + container_name[i] + " " + self.image_name[i]
            os.system(command)

    def save_status(self):
        now = time.localtime()
        current_time = "%02d%02d%02d%02d%02d%02d" % \
                       (now.tm_year % 100, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        print("Device is up as " + current_time)

        statusref = self.deviceref + '/status'
        ref = db.reference(statusref)
        ref.set(current_time)

    def exec_by_config(self):
        det_change = self.get_config()

        if det_change == 1:
            change_th = threading.Thread(target=self.change_by_config, name="change_th", )
            change_th.setDaemon(True)
            change_th.start()

        save_th = threading.Thread(target=self.save_status, name="save_th", )
        save_th.setDaemon(True)
        save_th.start()

        threading.Timer(5, self.exec_by_config, ).start()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("No projectID, Please input project ID")
        exit(1)

    projectID = sys.argv[1]
    cred = credentials.Certificate('./serviceAccountKey.json')
    firebase_admin = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://devicehub-e7c8d.firebaseio.com/'
    })

    try_time = 0
    while True:
        try_time += 1
        ip_address_dot = getdeviceip().split('.')
        ip_address = ''
        for i in range(len(ip_address_dot) - 1):
            ip_address = ip_address + ip_address_dot[i] + '-'
        ip_address = ip_address + ip_address_dot[len(ip_address_dot) - 1]

        projectref = 'projects/' + projectID
        deviceref = projectref + '/device/' + ip_address
        testref = db.reference(deviceref)

        if ((testref.get() != None)):
            if len(testref.get().keys()) >= 1:
                break

        print("There is no device config in Project... Try to refinding " + str(try_time))
        sys.stdout.write("\033[F")
        time.sleep(5)

    task = AsyncTask(deviceref)
    task.exec_by_config()

