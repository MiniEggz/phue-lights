# import bridge from connect script
from connect import b

# things that can be listed -- lights (and status), groups/rooms

# turn lights on and off -- e.g. turn OwenBedroom off / turn OwenBedroom on

# first argument will be the command type

# could create the commands with objects, but functions would be fine

##############################################################################

# ls (list function)
# takes either lights or groups/rooms
def ls(args):
    object = str.lower(args[0])
    rstring = ""
    if object == 'lights':
        print("\nLIGHTS:\n")
        for l in b.lights:
            print(f"NAME: {l.name}\tON: {l.on}")
        print()
    else:
        print(f"'{object}' is not a valid object to list.")
    

# turns a light on or off
def turn(args):

    if len(args) != 2:
        print("turn requires exactly 2 args - [light_name] and [status]")

    light_name = args[0]
    status = str.lower(args[1])

    if status != 'on' and status != 'off':
        return "ERROR: Status is not valid."

    if status == 'on':
        is_on = True
    else:
        is_on = False

    b.set_light(str(light_name), 'on', is_on)
    print(f"\nTurning light '{light_name}' {status}...\n")

# could create a turn all function where it will turn all lights in one room a certain colour


# command handler - takes list with each element being a word
def execute(command):
    method = str.lower(command[0])
    args = command[1:]
    if method == 'turn':
        turn(args)
    elif method == 'ls':
        ls(args)
    else:
        print(f"ERROR: '{method}' is not a valid command, type help for all valid commands.")

def artwork():
    print("""
   __                 __           ____                   
  / /  _______  ___  / /________  / / /__ ____  ___  __ __
 / _ \/ __/ _ \/ _ \/ __/ __/ _ \/ / / -_) __/ / _ \/ // /
/_//_/\__/\___/_//_/\__/_/  \___/_/_/\__/_/ (_) .__/\_, / 
                                             /_/   /___/ 
    """)

def start_CLI():
    artwork()
    while True:
        command = input(">> ")
        if command == 'exit':
            break
        execute(command.split())



if __name__ == "__main__":
    start_CLI()