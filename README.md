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

### User Statuses

There are 3 Statuses
1. LIVE
2. DEAD
3. GONE

Each one serves the purpose of selecting which users to Mute or Unmute.

## Command List

The commands are structured so that they are grouped into categories.

```
cbf rn
```