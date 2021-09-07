from phue import Bridge
import subprocess
import os
import re
import sys
import socket

import artwork

button_not_pressed_message = (
    "The link button has not been pressed in the last 30 seconds."
)

# get answer to yes/no question
def get_ans():
    while True:
        ans = str.lower(input('> '))
        if ans == 'y':
            return True
        elif ans == 'n':
            return False
        else:
            print('Error, invalid answer.')

def get_host_address_from_user():
    print("What is the first 3 components of your host ip address?")
    while True:
        host = input("> ")
        answer = input("Are you sure? (y/n): ")
        if get_ans():
            return host


# gets the host address (x.x.x.i) so can iterate through devices on the network
def get_host_address():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        local_ip = local_ip.split(".")
        if local_ip[0] == "127":
            local_ip = socket.gethostbyname(hostname + ".local")
            local_ip = local_ip.split(".")
        return f"{local_ip[0]}.{local_ip[1]}.{local_ip[2]}"
    except Exception:
        return get_host_address_from_user()

host_address = get_host_address()

# get all ips on the network
def get_iplist():
    print("finding all ip addresses on your network...")
    iplist = []
    raw = subprocess.getoutput("arp -a").split("\n")
    pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    for line in raw:
        match = pattern.search(line)
        if match is not None:
            iplist.append(match[0])
    print("found all ip adresses...")
    return iplist


# get all bridges on network given all ips
def get_bridge_iplist(iplist):
    print("finding ip addresses of all bridge devices on your network...")
    bridge_iplist = []
    for ip in iplist:
        try:
            # try to connect
            b = Bridge(ip)
            b.connect()
            b.lights  # double checks bridge is connected
            bridge_iplist.append(ip)
            print(f"{ip}: SUCCESS")
        except Exception as e:
            if button_not_pressed_message in str(e):
                bridge_iplist.append(ip)
                print(f"{ip}: SUCCESS")
            else:
                print(f"{ip}: FAIL")
    return bridge_iplist


# find first bridge on network given all ips
def get_first_bridge_ip(iplist):
    print("finding ip address of first bridge device on your network...")
    for ip in iplist:
        try:
            # try to connect
            b = Bridge(ip)
            b.connect()
            b.lights  # double checks bridge is connected
            print(f"{ip}: SUCCESS")
            write_ip(ip)
            return [ip]
        except Exception as e:
            if button_not_pressed_message in str(e):
                print(f"{ip}: SUCCESS")
                write_ip(ip)
                return [ip]
            else:
                print(f"{ip}: FAIL")
    return []  # empty if there is nothing found


# user to pick an option from a list
def get_index(iplist):
    while True:
        print("\nplease select one of these ip addresses\n")
        for i in range(0, len(iplist)):
            print(f"{i}: {iplist[i]}")
        ans = input("\n> ")
        try:
            ans = int(ans)
            if ans > -1 and ans < len(iplist):
                return ans
            else:
                print("\nthat was not a valid option")
        except Exception:
            print("that was not a valid option")


# select bridge from list of bridges
def select_bridge(iplist):
    ip = ""
    # may need to select which ip if more than one
    if len(iplist) == 1:
        ip = iplist[0]
    else:
        index = get_index(iplist)
        ip = iplist[index]
    return ip


def write_ip(ip):
    f = open("ip.txt", "w")
    f.write(ip)
    f.close()


def read_ip():
    f = open("ip.txt", "r")
    ip = f.read()
    f.close()
    return ip


# goes through all possible ips up to specified number
def get_generic_ip_list():
    return [f"{host_address}.{i}" for i in range(1, 255)]


# finds bridge and writes to ip.txt
def find_bridges(iplist):
    bridge_iplist = get_bridge_iplist(iplist)
    if len(bridge_iplist) > 0:
        bridge_ip = select_bridge(bridge_iplist)
        write_ip(bridge_ip)
        return True
    else:
        return False


# connect to the bridge, return bridge object and ip
def connect():
    while True:
        try:
            # try to connect using ip in ip.txt
            ip = read_ip()
            b = Bridge(ip)
            b.connect()
            b.lights
            print(f"Connected to bridge@{ip}\n")
            return b, ip
        except Exception as e:
            # bridge ip has been found but button needs to be pressed
            if button_not_pressed_message in str(e):
                print(
                    "cannot connect to bridge: please press button on bridge and press enter."
                )
                input()
            else:
                print()
                bridge = select_bridge(get_first_bridge_ip(get_generic_ip_list()))
                if not bridge:
                    return False, False


b, ip = connect()