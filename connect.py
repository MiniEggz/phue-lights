from phue import Bridge
from bridge_ip import ip
import subprocess
import os
import re

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
            print('SUCCESS')
        except Exception:
            print('FAILED')
    print('found all bridge ip addresses...')
    return bridge_iplist


if __name__ == '__main__':
    iplist = get_iplist()
    bridges = find_bridge_ip(iplist)
    print('\nBRIDGES:')
    for b in bridges:
        print(b)

#b = Bridge(ip)

# to connect, you must press the button in last 30 seconds
#b.connect()

# try to connect to the ip stored in the text file..

# if not, find the ip