from AMuteUsSettings import setChk
from commands import setup
from parsers import commandParser

if __name__ == "__main__":
    setChk()
    setup()
    while True:
        cmd = input("AMuteUs </> ")
        if len(cmd) == 0:
            continue
        commandParser(cmd.split("+"))