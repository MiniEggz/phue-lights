from phue import Bridge
from bridge_ip import ip
import subprocess
import os
import re
import sys

import artwork

button_not_pressed_message = 'The link button has not been pressed in the last 30 seconds.'

# get all ips on the network
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

# get all bridges on network given all ips
def get_bridge_iplist(iplist):
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

# user to pick an option from a list
def get_index(iplist):
    while True:
        print('\nplease select one of these ip addresses\n')
        for i in range (0,len(iplist)):
            print(f'{i}: {iplist[i]}')
        ans = input('\n> ')
        try:
            ans = int(ans)
            if ans > -1 and ans < len(iplist):
                return ans
            else:
                print('\nthat was not a valid option')
        except Exception:
            print('that was not a valid option')

# select bridge from list of bridges
def select_bridge(iplist):
    ip = ''
    # may need to select which ip if more than one
    if len(iplist) == 1:
        ip = iplist[0]
    else:
        index = get_index(iplist)
        ip = iplist[index]
    return ip

def write_ip(ip):
    f = open('ip.txt', 'w')
    f.write(ip)
    f.close()

def read_ip():
    f = open('ip.txt', 'r')
    ip = f.read()
    f.close()
    return ip

# connect to the bridge, return bridge object and ip
def connect():
    while True:
        try:
            # try to connect using ip in ip.txt
            ip = read_ip()
            b = Bridge(ip)
            b.connect()
            print(f'Connected to bridge@{ip}\n')
            return b, ip
        except Exception as e:
            # bridge ip has been found but button needs to be pressed
            if button_not_pressed_message in str(e):
                print('cannot connect to bridge: please press button on bridge and press enter.')
                input()
            else:
                # need to find the ip and store in ip.txt
                bridge_iplist = get_bridge_iplist(get_iplist())
                if len(bridge_iplist) > 0:
                    bridge_ip = select_bridge(bridge_iplist)
                    write_ip(bridge_ip)
                else:
                    return False, False

b, ip = connect()





#b = Bridge(ip)

# to connect, you must press the button in last 30 seconds
#b.connect()

# try to connect to the ip stored in the text file..

# if not, find the ip