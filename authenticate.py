import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "smartLock"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smartLock.settings")
import django
from django.conf import settings

django.setup()
from mylock.models import CustomUser

import serial
from mylock.main import authentication, backup_password

from django.http import HttpRequest

ser = serial.Serial('/dev/ttyACM0', 9600)

#pid = os.getpid()
#file = open('/home/pi/PID', 'w+')
#file.write(pid)
#file.close()

print("setup completed")

while True:
  while not ser.in_waiting:
    pass
  command = ser.readline().decode().rstrip()
  if "fingerprint_ID:" in command:
    fingerprint_ID = int(command.split(":")[1])
    print(fingerprint_ID)
    authentication(fingerprint_ID)
  elif command == "pincode":
    print("pincode")
    backup_password()
  print("done")
  command = ""
