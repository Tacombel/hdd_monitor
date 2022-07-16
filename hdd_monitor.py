import os

hddtemp = os.popen('hddtemp /dev/sdb /dev/sdc').readlines()
print(hddtemp)
for e in hddtemp:
    temp = e.split()[2]
    size = len(temp)
    temp = temp[:size-2]
    print(temp)