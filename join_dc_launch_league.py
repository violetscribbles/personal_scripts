# This script uses webbrowser.open and os.startfile to streamline my gaming experiences. 
# It opens League of Legends, Discord, u.gg and op.gg at the same time.

import os, webbrowser

def launch_apps(league, disco):
    os.startfile(league) # launches league
    os.startfile(disco) # launches discord

launch_apps('D:\\Games\League of Legends\LeagueClient.exe', 'C:\\Users\-REDACTED-\Desktop\Discord') # redacted personal directory

webbrowser.open("https://u.gg/", new=2) # opens u.gg in new tab
webbrowser.open("https://oce.op.gg/", new=2) # opens op.gg in a new tab
