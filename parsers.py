from commands import *

def commandParser(cmdList):
    for cmd in cmdList:
        match cmd[0]:
            case "0":
                parseMute(cmd)
            case "1":
                parseUnmute(cmd)
            case "5":
                parseDev(cmd)
            case "6":
                parseInfo(cmd)
            case "7":
                parseIgnored(cmd)
            case "8":
                parseUser(cmd)
            case "9":
                parseDead(cmd)
            case _:
                print("Invalid Command")

def parseMute(cmd):
    if len(cmd) > 1:
        match cmd[1]:
            case "0":
                muteAll()
            case "1":
                if len(cmd) > 2:
                    UID = int(cmd[2:])
                    ID = unamesList[UID-1]
                else:
                    ID = selectUser()
                if ID != 0:
                    muteUser(ID)
                    print(f"{ID} muted")
                else:
                    print("Cancelled")
    else:
        muteUndead()

def parseUnmute(cmd):
    if len(cmd) > 1:
        match cmd[1]:
            case "0":
                unmuteAll()
            case "1":
                if len(cmd) > 2:
                    UID = int(cmd[2:])
                    ID = unamesList[UID-1]
                else:
                    ID = selectUser()
                if ID != 0:
                    unmuteUser(ID)
                    print(f"{ID} unmuted")
                else:
                    print("Cancelled")
    else:
        unmuteUndead()

def parseDev(cmd):
    global dev
    if len(cmd) > 1:
        match cmd[1]:
            case "0":
                dev = False
                print("Developer Output Disabled")
            case "1":
                dev = True
                print("Developer Output Enabled")
    else:
        print(f"Dev Mode: {dev}")

def parseInfo(cmd):
    global stayGate, version
    if len(cmd) > 1:
        match cmd[1]:
            case "0":
                print("Closing AMuteUs...")
                stayGate = False
            case "1":
                print('Command List:\n-----------------------\n0 - mute\n\t00 - all\n\t01 - user\n1 - unmute\n\t10 - all\n\t11 - user\n5 - debug mode\n\t50 - off\n\t51 - on\n6 - program version\n\t60 - exit program\n\t61 - help\n7 - ignored list\n\t70 - reload\n\t71 - add\n8 - list users\n\t80 - list dead & ignored\n\t81 - list alive\n9 - deadlist\n\t90 - clear\n\t91 - add')
    else:
        print(f"AMuteUs {version}")

def parseIgnored(cmd):
    if len(cmd) > 1:
        match cmd[1]:
            case "0":
                reloadIgnoredList()
            case "1":
                if len(cmd) > 2:
                    UID = int(cmd[2:])
                    ID = unamesList[UID-1]
                else:
                    ID = selectUser()
                if ID != 0:
                    ignoredList.append(ID)
                    print(f"{ID} added to list")
                else:
                    print("Cancelled")
    else:
        listStatus(2)

def parseUser(cmd):
    if len(cmd) > 1:
        listStatus(int(cmd[1:]))
    else:
        listAllUsers

def parseDead(cmd):
    if len(cmd) > 1:
        match cmd[1]:
            case "0":
                clearDeadList()
            case "1":
                if len(cmd) > 2:
                    UID = int(cmd[2:])
                    ID = unamesList[UID-1]
                else:
                    ID = selectUser()
                if ID != 0:
                    ignoredList.append(ID)
                    print(f"{ID} added to Deadlist")
                else:
                    print("Cancelled")
    else:
        listStatus(0)