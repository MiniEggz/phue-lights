# import bridge from connect script
from connect import b
import time

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
        
search = 'Bedroom (Owen)'
for g in b.groups:
    if g.name == search:
        print("YAAYYY")