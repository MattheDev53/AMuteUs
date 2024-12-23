import requests
import json
from time import sleep
from AMuteUsSettings import *

def setup() -> None:
    """
    Sets up the program by fetching all usernames from the server and creating a user dictionary.
    This function should only be called once, at the start of the program.
    """
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
    """
    Unmutes all users in the user dictionary.
    
    Notes
    -----
    This function loops through the user dictionary and calls `unmuteUser` on each user. It then waits for `wait` seconds before continuing.
    """
    print("Unmuting All Users...")
    for user in userDict:
        unmuteUser(user)
        sleep(wait)
    print("All Users Unmuted!")

def muteAll() -> None:
    """
    Mutes all users in the user dictionary.
    
    Notes
    -----
    This function loops through the user dictionary and calls `muteUser` on each user. It then waits for `wait` seconds before continuing.
    """
    print("Muting All Users...")
    for user in userDict:
        muteUser(user)
        sleep(wait)
    print("All Users Muted!")

def unmuteUndead() -> None:
    """
    Unmutes all users with the status 'LIVE' in the user dictionary.

    Notes
    -----
    This function checks each user in the user dictionary. If a user's status is 'LIVE' (status code 1),
    it unmutes the user by calling `unmuteUser`. The function waits for `wait` seconds after each unmute operation.
    If the user is not 'LIVE', and developer mode is enabled, it will print a developer message indicating the user's status.
    Users in the ignored list are not affected by this function.
    """
    print("Unmuting Undead...")
    for user in userDict:
        if getUserStatus(user) == 1:
            unmuteUser(user)
            sleep(wait)
        else:
            if(dev==True):{print(f"[DEV] {user:-<32} [{userIndicator[getUserStatus(user)]:^4}]")}
    print("Unmuted Undead")

def muteUndead() -> None:
    """
    Mutes all users with the status 'LIVE' in the user dictionary.

    Notes
    -----
    This function checks each user in the user dictionary. If a user's status is 'LIVE' (status code 1),
    it mutes the user by calling `muteUser`. The function waits for `wait` seconds after each mute operation.
    If the user is not 'LIVE', and developer mode is enabled, it will print a developer message indicating the user's status.
    Users in the ignored list are not affected by this function.
    """
    print("Muting Undead...")
    for user in userDict:
        if getUserStatus(user) == 1:
            muteUser(user)
            sleep(wait)
        else:
            if(dev==True):{print(f"[DEV] {user:-<32} [{userIndicator[getUserStatus(user)]:^4}]")}
    print("Muted Undead")

def unmuteUser(username: str) -> None:
    """
    Unmutes the specified user on the Discord server.

    Parameters
    ----------
    username : str
        The username of the user to be unmuted.

    Notes
    -----
    This function sends a PATCH request to the Discord API to unmute the user. If developer mode is enabled,
    it will print a developer message indicating the request's result.
    """
    i = requests.patch(f"https://discord.com/api/v9/guilds/{guildID}/members/{userDict[username]}", json={"mute": False}, headers={'Authorization': dcToken})
    if(dev==True):{print(f"[DEV] {username:-<32} [{i.reason:^4}]")}

def muteUser(username: str) -> None:
    """
    Mutes the specified user on the Discord server.

    Parameters
    ----------
    username : str
        The username of the user to be muted.

    Notes
    -----
    This function sends a PATCH request to the Discord API to mute the user. If developer mode is enabled,
    it will print a developer message indicating the request's result.
    """
    i = requests.patch(f"https://discord.com/api/v9/guilds/{guildID}/members/{userDict[username]}", json={"mute": True}, headers={'Authorization': dcToken})
    if(dev==True):{print(f"[DEV] {username:-<32} [{i.reason:^4}]")}

def listAllUsers() -> None:
    """
    Lists all users with their respective statuses.

    Notes
    -----
    This function iterates through the list of usernames (`unamesList`) and prints each user's
    index, name, and status. The status is determined using the `getUserStatus` function and is
    displayed using the `userIndicator` list. The output is formatted to align the indices and usernames.
    """
    for index, user in enumerate(unamesList):
        print(f"[{index+1:->3}] {user:-<32} [{userIndicator[getUserStatus(user)]:^4}]")

def selectUser() -> str:
    """
    Lists all users and asks the user to select a user number.
    
    Notes
    -----
    Returns a blank string if the user enters in a non-digit character.
    """
    listAllUsers()
    uInput = input("Enter User Number: ")
    if uInput.isdigit():
        return unamesList[int(uInput)-1]
    else:
        return ""

def listStatus(statusCode: int) -> None:
    """
    Lists all users with a given status.

    Parameters
    ----------
    statusCode : int
        The status code to list users for.

    Notes
    -----
    This function iterates through the list of usernames (`unamesList`) and prints each user's
    index, name, and status if the user's status matches the given status code. The output is
    formatted to align the indices and usernames.
    """
    print(f"{userIndicator[statusCode]} Users:")
    for index, user in enumerate(unamesList):
        if getUserStatus(user) == statusCode:
            print(f"[{index+1:->3}] {user:-<32} [{userIndicator[getUserStatus(user)]:^4}]")

def getUserStatus(username: str) -> int:
    """
    Gets the status of the specified user.

    Parameters
    ----------
    username : str
        The username of the user to get the status of.

    Returns
    -------
    int
        The status of the user. The status codes are as follows:
        0 - Dead
        1 - Alive
        2 - Ignored

    Notes
    -----
    This function checks if the user is in the dead list or ignored list and returns the appropriate status.
    If the user is not in either list, it returns a status of 1, indicating the user is alive.
    """
    if username in ignoredList:
        return 2
    if username in deadList:
        return 0
    return 1

def userOnline(username: str) -> bool:
    """
    Checks if a user is online.

    Parameters
    ----------
    username : str
        The username of the user to check.

    Returns
    -------
    bool
        True if the user is online, False otherwise.

    Notes
    -----
    This function sends a GET request to the Discord API to get the user's status, and then sends a PATCH request with the same
    mute status to check if the request is successful. If the request is successful, it returns True, otherwise it returns False.
    """
    i = requests.get(f"https://discord.com/api/v9/guilds/{guildID}/members/{userDict[username]}", headers={'Authorization': dcToken})
    temp = json.loads(i.text)
    i = requests.patch(f"https://discord.com/api/v9/guilds/{guildID}/members/{userDict[username]}", json={"mute": temp['mute']}, headers={'Authorization': dcToken})
    if(dev==True):{print(f"[DEV] {username:-<32} [{i.reason:^4}]")}
    if i.reason == "Bad Request":
        return False
    return True

def reloadIgnoredList() -> None:
    """
    Reloads the ignored list by going through all users in the user dictionary and checking if they are online.
    If a user is not online, they are added to the ignored list.
    """
    global ignoredList
    print("Reloading Ignored List...")
    for i in range(len(ignoredList)):
        ignoredList.pop()
    for user in userDict:
        if userOnline(user) == False:
            ignoredList.append(user)
    print("Ignored List Reloaded")

def clearDeadList() -> None:
    """
    Clears the dead list by unmuting all users in the list and then emptying the list.
    """
    global deadList
    print("Clearing Deadlist...")
    for i in range(len(deadList)):
        unmuteUser(deadList.pop())
    print("Deadlist Cleared!")

def delay(secs: int) -> None:
    """
    Delays the program for the specified number of seconds.

    Parameters
    ----------
    secs : int
        The number of seconds to delay the program.
    """
    print(f"Delaying for {secs} seconds...")
    sleep(secs)

if __name__ == "__main__":
    print("This file is not intended to be run directly. Please run main.py instead.")