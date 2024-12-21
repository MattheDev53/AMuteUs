from AMuteUsSettings import setChk
from commands import setup
from parsers import commandParser


setChk()
setup()
stayGate = True
while stayGate:
    cmd = input("AMuteUs </> ")
    if len(cmd) == 0:
        continue
    commandParser(cmd.split("+"))