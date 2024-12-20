# AMuteUs

## The Problem

Have you ever played the hit game Among Us with your friends, but some of your friends don't have consoles/PCs and only have phones? Have you ever felt the annoyance of needing to individually server mute your friends? Me too.

## The Solution 

That's the inspiration for creating AMuteUs. A relatively robust Python program for muting & unmuting people in Discord. It utilizes HTTP Requests to mute all of your friends in a Discord VC.

## The Meaty Goods

This program has features that set it apart from what I've seen out there

### No Messing With Bots

The bulk of solutions I've seen require Bots to be added to the server, meaning time spent creating, getting the token, yadda yadda. In contrast, AMuteUs just uses *your* Discord Token. No Bot Setup = No BS.

### Efficiency

I spent many months before releasing this to GitHub trying to make this program as efficient as possible. The only thing stopping it now is Python being slow (although between you and me I wouldn't be able to tell a difference either way)

### User Lists

The User Lists are a life saver for efficiency, and player death management. There are 2 main lists, The Deadlist and The Ignored List. These help differentiate between people who are

- Gone
- Alive
OR
- Dead

Making it easy to control who speaks and who doesn't

## Command List

The commands are structured so that they are grouped into categories.

**NOTICE**: This list is changing to be only the numerical commands for efficiency, ease of writing/changing, & added functionality

```
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
```