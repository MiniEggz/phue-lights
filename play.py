# import bridge from connect script
from connect import b
import time
from datetime import datetime
import threading

lights = b.lights

# b.set_light('OwenBedroom', 'on', True)
def flash():
    pulses = 3
    while pulses > 0:
        b.set_light('OwenBedroom', 'on', False)
        time.sleep(1)
        b.set_light('OwenBedroom', 'on', True)
        time.sleep(1)
        pulses -= 1
        
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def wakemeup():

    wake_time = datetime(2021, 6, 21, 22, 50)

    while True:
        if datetime.now() > wake_time:
            b.set_light("OwenBedroom", 'on', False)
            break

while True:
    command = input(">> ")
    if command == "exit":
        exit()
    elif command == "start":
        thread = threading.Thread(target=wakemeup)
        thread.start()
    else:
        print("blaaa")