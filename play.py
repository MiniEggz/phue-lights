# import bridge from connect script
from connect import b
import time

print(b.name)

print(b)

lights = b.lights

# b.set_light('OwenBedroom', 'on', True)

pulses = 3
while pulses > 0:
    b.set_light('OwenBedroom', 'on', False)
    time.sleep(1)
    b.set_light('OwenBedroom', 'on', True)
    time.sleep(1)
    pulses -= 1