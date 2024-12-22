from AMuteUsSettings import setChk
from commands import setup
from parsers import commandParser


setChk()
setup()
while True:
    cmd = input("AMuteUs </> ")
    if len(cmd) == 0:
        continue
    commandParser(cmd.split("+"))