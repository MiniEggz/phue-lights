from phue import Bridge
from bridge_ip import ip

b = Bridge(ip)

# to connect, you must press the button in last 30 seconds
b.connect()
