# Your Token
dcToken = None
# The ID of the Server you want to mute
guildID = None
# List of User IDs you want to mute
UIDs = None
# Waiting time between operations
wait = 0.5
# Developer mode flag
dev = False
# !! LEAVE AS IS !!
deadList = []
# !! LEAVE AS IS !!
ignoredList = []
# !! LEAVE AS IS !!
unamesList = []
# !! LEAVE AS IS !!
userDict = {}
# !! LEAVE AS IS !! (or don't, it's not gonna break anything (maybe))
version = "v2024.12.23.4"
# Indicators for user status
userIndicator = ["DEAD", "LIVE", "GONE"]

def setChk():
    """
    Checks if all settings are set. If any are not set, then it will print out a message telling the user which ones are missing and exit the program.
    If all are set, it will print out a success message and exit.
    """
    global dcToken, guildID, UIDs
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
            print("\tMissing Discord Token")
        if checking & 0b010 == 0b010:
            print("\tMissing Guild ID")
        if checking & 0b100 == 0b100:
            print("\tMissing User IDs")
        print("Please Edit AMuteUsSettings.py")
        exit()
    print("All Settings Found!")
    return True

if __name__ == "__main__":
    if setChk():
        print("Please run main.py to start the script.")