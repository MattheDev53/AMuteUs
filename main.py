import requests
import json
from time import sleep
from AMuteUsSettings import dcToken, guildID, UIDs

version = "v2024.12.19.0"
unamesList = []
checking = 0b000

if dcToken == None:
    checking += 0b001
if guildID == None:
    checking += 0b010
if UIDs == None:
    checking += 0b100

if checking != 0b000:
    print("AMuteUs Settings Missing Settings:")
    if checking & 0b001 == 0b001:
        print("  Missing Discord Token")
    if checking & 0b010 == 0b010:
        print("  Missing Guild ID")
    if checking & 0b100 == 0b100:
        print("  Missing User IDs")
    print("Please Edit AMuteUsSettings.py and run the script again.")
    exit()
print("All Settings Found!")
# Loop through UIDs to get usernames for easier reading
for user in range(len(UIDs)):
    print(f"Fetching Username {user+1} of {len(UIDs)}")
    i = requests.get(f"https://discord.com/api/v9/guilds/{guildID}/members/{UIDs[user]}", headers={'Authorization': dcToken})
    temp = json.loads(i.text)
    print(i.reason)
    unamesList.append(temp['user']['username'])
    print(f"User {temp['user']['username']} fetched!")
print("All Usernames Fetched!")

print("Creating User Dictionary...")
userDict = {}.fromkeys(unamesList)

print("Adding UIDs to User Dictionary...")
index = 0
for where in userDict:
    print(f"Adding UID {index+1} of {len(unamesList)}")
    userDict[where] = UIDs[index]
    index += 1
print("User Dictionary Created!")

print("Setting Additional Variables...")
wait = 0.5
dev = True
deadList = []
ignoredList = []
userIndicator = ["DEAD", "LIVE", "GONE"]

print("Defining Functions...")

def unmuteAll():
    print("Unmuting All Users...")
    for user in userDict:
        unmuteUser(user)
        sleep(wait)
    print("All Users Unmuted!")

def muteAll():
    print("Muting All Users...")
    for user in userDict:
        muteUser(user)
        sleep(wait)
    print("All Users Muted!")

def unmuteUndead():
    print("Unmuting Undead...")
    for user in userDict:
        if getUserStatus(user) == 1:
            unmuteUser(user)
            sleep(wait)
        else:
            if(dev==True):{print(f"[DEV] {user:-<32} [{userIndicator[getUserStatus(user)]:^4}]")}
    print("Unmuted Undead")

def muteUndead():
    print("Muting Undead...")
    for user in userDict:
        if getUserStatus(user) == 1:
            muteUser(user)
            sleep(wait)
        else:
            if(dev==True):{print(f"[DEV] {user:-<32} [{userIndicator[getUserStatus(user)]:^4}]")}
    print("Muted Undead")

def unmuteUser(username):
    i = requests.patch(f"https://discord.com/api/v9/guilds/{guildID}/members/{userDict[username]}", json={"mute": False}, headers={'Authorization': dcToken})
    if(dev==True):{print(f"[DEV] {username:-<32} [{i.reason:^4}]")}

def muteUser(username):
    i = requests.patch(f"https://discord.com/api/v9/guilds/{guildID}/members/{userDict[username]}", json={"mute": True}, headers={'Authorization': dcToken})
    if(dev==True):{print(f"[DEV] {username:-<32} [{i.reason:^4}]")}

def listAllUsers():
    for user in range(len(unamesList)):
        print(f"[{user+1:->3}] {unamesList[user]:-<32} [{userIndicator[getUserStatus(unamesList[user])]:^4}]")

def selectUser():
    listAllUsers()
    uInput = input("Enter User Number: ")
    if uInput.isdigit():
        return unamesList[int(uInput)-1]
    else:
        return 0

def listStatus(statusCode):
    for user in range(len(unamesList)):
        if getUserStatus(unamesList[user]) == statusCode:
            print(f"[{user+1:->3}] {unamesList[user]:-<32} [{userIndicator[getUserStatus(unamesList[user])]:^4}]") 

def getUserStatus(username):
    if username in deadList:
        return 0
    if username in ignoredList:
        return 2
    return 1

def userOnline(username):
    i = requests.get(f"https://discord.com/api/v9/guilds/{guildID}/members/{userDict[username]}", headers={'Authorization': dcToken})
    temp = json.loads(i.text)
    i = requests.patch(f"https://discord.com/api/v9/guilds/{guildID}/members/{userDict[username]}", json={"mute": temp['mute']}, headers={'Authorization': dcToken})
    if(dev==True):{print(f"[DEV] {username:-<32} [{i.reason:^4}]")}
    if i.reason == "Bad Request":
        return False
    return True

def reloadIgnoredList():
    global ignoredList
    print("Reloading Ignored List...")
    ignoredList = []
    for user in userDict:
        if userOnline(user) == False:
            ignoredList.append(user)
    print("Ignored List Reloaded")

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
                print('Command List:\n-----------------------\n0 - mute\n\t00 - all\n\t01 - user\n1 - unmute\n\t10 - all\n\t11 - user\n5 - debug mode\n\t50 - off\n\t51 - on\n6 - program version\n\t60 - exit program\n\t61 - help\n7 - ignored list\n\t70 - reload\n\t71 - add\n8 - list users\n\t80 - list dead & ignored\n\t81 - list alive\n9 - deadlist\n\t90 - clear\n\t91 - add\n.. - exit')
    else:
        print(f"AMuteUs {version}")

def parseIgnored(cmd):
    print(f"unfinished cmd={cmd}")

def parseUser(cmd):
    print(f"unfinished cmd={cmd}")

def parseDead(cmd):
    print(f"unfinished cmd={cmd}")

print("Optimizing User List...")
reloadIgnoredList()
print("Starting AMuteUs...")
print("\n+-----------------------------------------------+\n|    ___    __  ___      __           __  __    |\n|   /   |  /  |/  /_  __/ /____      / / / /____|\n|  / /| | / /|_/ / / / / __/ _ \\    / / / / ___/|\n| / ___ |/ /  / / /_/ / /_/  __/   / /_/ (__  ) |\n|/_/  |_/_/  /_/\\__,_/\\__/\\___/    \\____/____/  |\n+-----------------------------------------------+\nType '61' for command list\nType '60' to exit\n\n\n")
stayGate = True
while stayGate:
    cmd = input("AMuteUs </> ")
    if len(cmd) == 0:
        continue
    commandParser(cmd.split("+"))
    '''
    match cmd:
        case "91":
            ID = selectUser()
            if ID != 0:
                deadList.append(ID)
                print(f"{ID} added to Deadlist")
            else:
                print("Cancelled")
        case "90":
            for user in deadList:
                unmuteUser(user)
            deadList = []
            print("Deadlist Cleared")
        case "9":
            listStatus(0)
        case "71":
            ID = selectUser()
            if ID != 0:
                ignoredList.append(ID)
                print(f"{ID} added to Ignored List")
            else:
                print("Cancelled")
        case "70":
            reloadIgnoredList()
        case "7":
            listStatus(2)
        case "8":
            listAllUsers()
        case "80":
            listStatus(0)
            listStatus(2)
        case "81":
            listStatus(1)
        case _:
            print("Invalid Command")
        '''

