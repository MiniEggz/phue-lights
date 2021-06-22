# import bridge from connect script
'''
from connect import b
import time
from datetime import datetime
import threading
import platform
import os

lights = b.lights

# b.set_light('OwenBedroom', 'on', True)
def flash():
    pulses = 5
    while pulses > 0:
        b.set_light('OwenBedroom', 'on', False)
        time.sleep(0.5)
        b.set_light('OwenBedroom', 'on', True)
        time.sleep(0.5)
        pulses -= 1
        
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def wakemeup():

    wake_time = datetime(2021, 6, 21, 22, 50)

    while True:
        if datetime.now() > wake_time:
            b.set_light("OwenBedroom", 'on', False)
            break

print(platform.system())

'''

for i in range (0,2):
    print(i)