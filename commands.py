import requests
import json
from time import sleep
from AMuteUsSettings import *

def setup() -> None:
    global unamesList, userDict, UIDs
    print("Fetching Usernames...")
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
    
    print("Optimizing User List...")
    reloadIgnoredList()
    print("Starting AMuteUs...")
    print("\n+-----------------------------------------------+\n|    ___    __  ___      __           __  __    |\n|   /   |  /  |/  /_  __/ /____      / / / /____|\n|  / /| | / /|_/ / / / / __/ _ \\    / / / / ___/|\n| / ___ |/ /  / / /_/ / /_/  __/   / /_/ (__  ) |\n|/_/  |_/_/  /_/\\__,_/\\__/\\___/    \\____/____/  |\n+-----------------------------------------------+\nType '61' for command list\nType '60' to exit\n\n\n")

def unmuteAll() -> None:
    print("Unmuting All Users...")
    for user in userDict:
        unmuteUser(user)
        sleep(wait)
    print("All Users Unmuted!")

def muteAll() -> None:
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

def clearDeadList():
    global deadList
    for user in deadList:
        unmuteUser(user)
    deadList = []
    print("Deadlist Cleared!")