from phue import Bridge
from bridge_ip import ip
import subprocess
import os
import re
import sys

button_not_pressed_message = 'The link button has not been pressed in the last 30 seconds.'

def get_iplist():
    print('finding all ip addresses on your network...')
    iplist = []
    raw = subprocess.getoutput('arp -a').split('\n')
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    for line in raw:
        match = pattern.search(line)
        if match is not None:
            iplist.append(match[0])
    print('found all ip adresses...')
    return iplist

def find_bridge_ip(iplist):
    print('finding ip addresses of all bridge devices on your network...')
    bridge_iplist = []
    for ip in iplist:
        try:
            b = Bridge(ip)
            b.connect()
            bridge_iplist.append(ip)
        except Exception as e:
            if button_not_pressed_message in str(e):
                bridge_iplist.append(ip)

    if len(bridge_iplist) == 0:
        print('no bridge ip addresses were found.')
    else:
        print('found all bridge ip addresses...')
        print('\nBRIDGES:')
        for b in bridge_iplist:
            print(b)
    return bridge_iplist


if __name__ == '__main__':
    iplist = get_iplist()
    bridges = find_bridge_ip(iplist)
    print(bridges)

#b = Bridge(ip)

# to connect, you must press the button in last 30 seconds
#b.connect()

# try to connect to the ip stored in the text file..

# if not, find the ip