# import bridge from connect script
from connect import b

import datetime
import time
# things that can be listed -- lights (and status), groups/rooms

# turn lights on and off -- e.g. turn OwenBedroom off / turn OwenBedroom on

# first argument will be the command type

# could create the commands with objects, but functions would be fine


#################
#               #
#   UTILITIES   #
#               #
#################

def get_group(group_name):
    for g in b.groups:
        if g.name == group_name:
            return g



##################
#                #
#    COMMANDS    #
#                #
##################

# ls (list function)
# takes either lights or groups/rooms
def ls(args):
    if len(args) != 1:
        print("ERROR: 'ls' takes exactly 1 argument - [object]")
        return

    object = str.lower(args[0])
    rstring = ""
    if object == 'lights':
        print("\nLIGHTS:\n")
        for l in b.lights:
            print(f"NAME: {l.name}\tON: {l.on}")
        print()
    elif object == 'groups' or object == 'rooms':
        print("\nGROUPS\n")
        for g in b.groups:
            print(f"NAME: {g.name}")
            print("LIGHTS: ")
            for l in g.lights:
                print(f"\tNAME: {l.name}\tON: {l.on}")
            print()
    else:
        print(f"'{object}' is not a valid object to list.")
    

# turns a light on or off
def turn(args):
    if len(args) != 2:
        print("ERROR: 'turn' takes exactly 2 args - [light_name] and [on/off]")

    light_name = args[0]
    status = str.lower(args[1])

    if status != 'on' and status != 'off':
        print("ERROR: Status is not valid.")
        return

    if status == 'on':
        is_on = True
    else:
        is_on = False

    print(f"\nTurning light '{light_name}' {status}...\n")
    b.set_light(str(light_name), 'on', is_on)

# turns all lights in one group/room on or off
def turnall(args):

    if len(args) != 2:
        print("ERROR: 'turnall' takes exactly 2 args - [group_name] and [on/off]")
        return

    group_name = args[0]
    status = str.lower(args[1])

    if status != 'on' and status != 'off':
        print("ERROR: Status is not valid.")
        return
    
    if status == 'on':
        is_on = True
    else:
        is_on = False

    g = get_group(group_name)
    try:
        g.on = is_on
        print(f"\nTurning all lights in '{group_name}' {status}\n")
    except Exception:
        print("ERROR: this group does not exist.")

# change brightness of lights given name and brightness
def brightness(args):
    if len(args) != 2:
        print("ERROR: 'brightness' takes exactly 2 args - [light_name] and [brightness(0-255)]")
        return
    
    try:
        int(args[1])
    except Exception:
        print("ERROR: a number was not entered for the brightness.")
        return

    light_name = args[0]
    brightness = int(args[1])

    print(f"\nSetting {light_name} brightness to {brightness}\n")
    b.set_light(light_name, 'bri', brightness)

# change brightness of all lights in a group/room
def brightnessall(args):
    if len(args) != 2:
        print("ERROR: 'brightnessall' takes exactly 2 args - [light_name] and [brightness(0-255)]")
        return
    
    try:
        int(args[1])
    except Exception:
        print("ERROR: a number was not entered for the brightness.")
        return

    group_name = args[0]
    brightness = int(args[1])

    g = get_group(group_name)

    try:
        print(f"\nSetting {group_name} brightness to {brightness}\n")
        g.brightness = brightness
    except Exception:
        print("ERROR: this group name does not exist.")

def wakemeup(args):
    if len(args) != 3:
        print("ERROR: 'wakemeup takes exactly 3 arguments - [light_name] [hour] [minute]")
        return
    
    try:
        for i in args[1:]:
            int(i)
    except Exception:
        print("ERROR: at least one of the arguments is not an integer.")

    light_name = args[0]
    hours = int(args[1])
    mins = int(args[2])

    now = datetime.datetime.now()
    wake_time = datetime.datetime(now.year, now.month, now.day, hours, mins)

    if wake_time < now:
        day = "tomorrow"
        wake_time += datetime.timedelta(days=1)
    else:
        day = "today"
    
    print(f"Waiting to wake you up at {wake_time.hour}:{wake_time.minute} {day}...")
    
    while True:
        if datetime.datetime.now() > wake_time:
            b.set_light(light_name, 'on', True)
            print("Wakey wakey...\n")
            break





# needs to be vetted to allow spaces when quotation marks are used
# this only allows one space max between words
def split(command):
    command = command.split()
    vetted_commands = []
    # variable to store combination
    comb = ""
    add_to_comb = False
    for i in command:
        if i[0] == '"':
            comb += i[1:]
            add_to_comb = True
        elif i[-1] == '"':
            comb += " " + i[:-1]
            vetted_commands.append(comb)
            comb = ""
            add_to_comb = False
        else:
            if add_to_comb == True:
                comb += " " + i
            else:
                vetted_commands.append(i)
    return vetted_commands

# command handler - takes list with each element being word from command
def execute(command):
    method = str.lower(command[0])
    args = command[1:]
    if method == 'turn':
        turn(args)
    elif method == 'ls':
        ls(args)
    elif method == 'turnall':
        turnall(args)
    elif method == "brightness":
        brightness(args)
    elif method == "brightnessall":
        brightnessall(args)
    elif method == "wakemeup":
        wakemeup(args)
    else:
        print("ERROR: Invalid command, type help for all valid commands.")

def artwork():
    print("""\n
   __                 __           ____                   
  / /  _______  ___  / /________  / / /__ ____  ___  __ __
 / _ \/ __/ _ \/ _ \/ __/ __/ _ \/ / / -_) __/ / _ \/ // /
/_//_/\__/\___/_//_/\__/_/  \___/_/_/\__/_/ (_) .__/\_, / 
                                             /_/   /___/ 
    \n""")

def start_CLI():
    artwork()
    while True:
        command = input(">> ")
        if str.lower(command) == 'exit':
            break
        execute(split(command))



if __name__ == "__main__":
    start_CLI()


"""
TODO:
change names of lights and groups

change colour of lights
change colour of groups

set wake up times and stuff

"""