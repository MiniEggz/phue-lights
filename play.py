# import bridge from connect script

from connect import b
import colorsys
import time
from datetime import datetime
import threading
import platform
import os

lights = b.lights

# b.set_light('OwenBedroom', 'on', True)
def flash():
    pulses = 5
    b.set_light('OwenColour', 'hue', 20)
    b.set_light('OwenColour', 'sat', 255)
    while pulses > 0:
        b.set_light('OwenColour', 'on', False)
        time.sleep(1)
        b.set_light('OwenColour', 'on', True)
        time.sleep(1)
        pulses -= 1
    b.set_light('OwenColour', 'sat', 0)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def wakemeup():
    wake_time = datetime(2021, 6, 21, 22, 50)
    while True:
        if datetime.now() > wake_time:
            b.set_light("OwenBedroom", 'on', False)
            break

#b.set_light('OwenColour', 'xy', [1,1])
#b.set_light('OwenColour', 'hue', 20)
#b.set_light('OwenColour', 'sat', 0)

#b.set_light('OwenColour', 'hue', 0)
# max 65535
#flash()

rgb = ['255', '255', '255']
'''
h, s, v = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
print(h)
print(s)
print(v)

b.set_light('OwenColour', 'hue', int(round(h * 65535)))
b.set_light('OwenColour', 'sat', int(round(s * 255)))
b.set_light('OwenColour', 'bri', int(round(v)))
'''
for i in range (0,len(rgb)):
    rgb[i] = int(rgb[i])

for x in rgb:
    print(x+1)