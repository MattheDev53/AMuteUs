from commands import *

def commandParser(cmdList: list) -> None:
    """
    Parses a list of commands and delegates each command to the appropriate parser function.

    Parameters
    ----------
    cmdList : list
        A list of commands, where each command is a string. The first character of each command
        determines which parser function is called.

    Notes
    -----
    - Commands starting with "0" are parsed by `parseMute`.
    - Commands starting with "1" are parsed by `parseUnmute`.
    - Commands starting with "5" are parsed by `parseDev`.
    - Commands starting with "6" are parsed by `parseInfo`.
    - Commands starting with "7" are parsed by `parseIgnored`.
    - Commands starting with "8" are parsed by `parseUser`.
    - Commands starting with "9" are parsed by `parseDead`.
    - An "Invalid Command" message is printed for unrecognized commands.
    """

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

def parseMute(cmd: str):
    """
    Parse the mute command.

    Parameters
    ----------
    cmd : str
        The command to parse.

    Notes
    -----
    If the command is "00", it will mute all users.
    If the command is "01", it will mute a user selected by the user.
    If the command is "0" only, it will mute all undead users.
    """
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
                if ID != "":
                    muteUser(ID)
                    print(f"{ID} muted")
                else:
                    print("Cancelled")
    else:
        muteUndead()

def parseUnmute(cmd: str):
    """
    Parse the unmute command.

    Parameters
    ----------
    cmd : str
        The command to parse.

    Notes
    -----
    If the command is "10", it will unmute all users.
    If the command is "11", it will unmute a user selected by the user.
    If the command is "1" only, it will unmute all undead users.
    """
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
                if ID != "":
                    unmuteUser(ID)
                    print(f"{ID} unmuted")
                else:
                    print("Cancelled")
    else:
        unmuteUndead()

def parseDev(cmd: str):
    """
    Parse the dev command.

    Parameters
    ----------
    cmd : str
        The command to parse.

    Notes
    -----
    If the command is "50", it will disable developer output.
    If the command is "51", it will enable developer output.
    If the command is "5" only, it will print out the current state of developer mode.
    """
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

def parseInfo(cmd: str):
    """
    Parse the info command.

    Parameters
    ----------
    cmd : str
        The command to parse.

    Notes
    -----
    If the command is "60", it will exit the program.
    If the command is "61", it will print out the command list.
    If the command is "6" only, it will print out the program's version.
    """
    global stayGate, version
    if len(cmd) > 1:
        match cmd[1]:
            case "0":
                print("Closing AMuteUs...")
                exit()
            case "1":
                print('Command List:\n-----------------------\n0 - mute\n\t00 - all\n\t01 - user\n1 - unmute\n\t10 - all\n\t11 - user\n5 - debug mode\n\t50 - off\n\t51 - on\n6 - program version\n\t60 - exit program\n\t61 - help\n7 - ignored list\n\t70 - reload\n\t71 - add\n8 - list users\n\t80 - list dead & ignored\n\t81 - list alive\n9 - deadlist\n\t90 - clear\n\t91 - add')
    else:
        print(f"AMuteUs {version}")

def parseIgnored(cmd: str):
    """
    Parse the ignored command.

    Parameters
    ----------
    cmd : str
        The command to parse.

    Notes
    -----
    If the command is "70", it will reload the ignored list.
    If the command is "71", it will add the user to the ignored list.
    If the command is "7" only, it will list all users in the ignored list.
    """
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
                if ID != "":
                    ignoredList.append(ID)
                    print(f"{ID} added to list")
                else:
                    print("Cancelled")
    else:
        listStatus(2)

def parseUser(cmd: str):
    """
    Parse the user command.

    Parameters
    ----------
    cmd : str
        The command to parse.

    Notes
    -----
    If the command is only "8", it will list all users.
    If the command is "8" followed by a number, it will list the users with that status.
    """
    if len(cmd) > 1:
        listStatus(int(cmd[1:]))
    else:
        listAllUsers

def parseDead(cmd: str):
    """
    Parse the dead command.

    Parameters
    ----------
    cmd : str
        The command to parse.

    Notes
    -----
    If the command is "90", it will clear the deadlist.
    If the command is "91", it will add the user to the deadlist.
    If the command is "9" only, it will list all users in the deadlist.
    """
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
                if ID != "":
                    ignoredList.append(ID)
                    print(f"{ID} added to Deadlist")
                else:
                    print("Cancelled")
    else:
        listStatus(0)