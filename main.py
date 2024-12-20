import requests
import json
from time import sleep
from AMuteUsSettings import dcToken, guildID, UIDs

version = "v2024.12.19.0 [{}]"
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
dev = False
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
        return True
    return False

def reloadIgnoredList():
    global ignoredList
    print("Reloading Ignored List...")
    ignoredList = []
    for user in userDict:
        if userOnline(user) == False:
            ignoredList.append(user)
    print("Ignored List Reloaded")

print("Optimizing User List...")
reloadIgnoredList()
print("Starting AMuteUs...")
print("\n+-----------------------------------------------+\n|    ___    __  ___      __           __  __    |\n|   /   |  /  |/  /_  __/ /____      / / / /____|\n|  / /| | / /|_/ / / / / __/ _ \\    / / / / ___/|\n| / ___ |/ /  / / /_/ / /_/  __/   / /_/ (__  ) |\n|/_/  |_/_/  /_/\\__,_/\\__/\\___/    \\____/____/  |\n+-----------------------------------------------+\nType 'help' or '61' for command list\nType 'exit' or '60' or '..' to exit\n\n\n")
cmd = ""
while cmd != "exit":
    cmd = input("AMuteUs </> ")
    match cmd:
        case "ua" | "10":
            unmuteAll()
        case "ma" | "00":
            muteAll()
        case "uu" | "11":
            ID = selectUser()
            if ID != 0:
                unmuteUser(ID)
                print(f"{ID} muted")
            else:
                print("Cancelled")
        case "mu" | "01":
                muteUser(ID)
                print(f"{ID} muted")
        case "m" | "0":
            muteUndead()
        case "u" | "1":
            unmuteUndead()
        case "adl" | "91":
            ID = selectUser()
            if ID != 0:
                deadList.append(ID)
                print(f"{ID} added to Deadlist")
            else:
                print("Cancelled")
        case "cdl" | "90":
            for user in deadList:
                unmuteUser(user)
            deadList = []
            print("Deadlist Cleared")
        case "qdl" | "9":
            listStatus(0)
        case "ail" | "71":
            ID = selectUser()
            if ID != 0:
                ignoredList.append(ID)
                print(f"{ID} added to Ignored List")
            else:
                print("Cancelled")
        case "ril" | "70":
            reloadIgnoredList()
        case "qil" | "7":
            listStatus(2)
        case "l" | "8":
            listAllUsers()
        case "lg" | "80":
            listStatus(0)
            listStatus(2)
        case "la" | "81":
            listStatus(1)
        case "dt" | "51":
            dev = True
            print("Developer Output Enabled")
        case "df" | "50":
            dev = False
            print("Developer Output Disabled")
        case "d" | "5":
            print(f"Dev Mode: {dev}")
        case "v" | "6":
            print("AMuteUs {version}")
        case "help" | "61":
            print('''
Simple Command List:
-------------------
u - unmute
  ua - unmute all
  uu - unmute user
m - mute
  ma - mute all
  mu - mute user
d - debug mode
  df - off
  dt - on
v - version
exit - exit program
help - help screen
l - list users
  lg - list dead & ignored
  la - list alive
qdl - query deadlist
cdl - clear deadlist
adl - add to deadlist
qil - query ignoredlist
cil - clear ignoredlist
ail - add to ignoredlist


Advanced Command List:
-----------------------
0 - mute
  00 - all
  01 - user
1 - unmute
  10 - all
  11 - user
5 - debug mode
  50 - off
  51 - on
6 - program version
  60 - exit program
  61 - help
7 - ignored list
  70 - reload
  71 - add
8 - list users
  80 - list dead & ignored
  81 - list alive
9 - deadlist
  90 - clear
  91 - add
.. - exit program
''')
        case "exit" | ".." | "60":
            print("Closing AMuteUs...")
            cmd = "exit"
        case "":
            continue
        case _:
            print("Invalid Command")

