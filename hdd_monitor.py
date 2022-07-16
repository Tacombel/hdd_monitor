# python 3.8.10

from config import Config
import os
import json
from requests import post


cmd = "hddtemp"
for e in Config.paths:
    cmd = cmd + " " + e
hddtemp = os.popen(cmd).readlines()
print(hddtemp)
disks = Config.disks

n = 0
for e in hddtemp:
    temp = e.split()[2]
    size = len(temp)
    temp_data = {"attributes": {"unit_of_measurement": "°C"}}
    temp_data["state"] = temp[:size-2]
    url = "http://" + Config.HA_server + ":8123/api/states/sensor." + Config.server + "_temp_" + disks[n]
    print(url)
    headers = {
        "Content-Type": "application/json",
    }
    headers["Authorization"] = "Bearer " + Config.token
    data = json.dumps(temp_data)
    response = post(url, headers=headers, data=data)

    print(response.text)
    print(response)
    n +=1
    