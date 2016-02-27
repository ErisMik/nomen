"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

import webbrowser
import requests
from library import tools

CONF_DATA = {}

# Determine steam id
KNOW_STEAM = raw_input("Do you know your steam id number? (yes or no): ")
if "n" in KNOW_STEAM:
    webbrowser.open("http://steamidfinder.com/", new=1)
    webbrowser.open("https://store.steampowered.com//login/?redir=0", new=1)
CONF_DATA["steam_id"] = raw_input("What is your steamid64 number?")

# Detrmine league id
SUMMONER_NAME = raw_input("What is your league summoner name?")
API_URL = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{name}?api_key={key}"
SUMMONER_DATA = requests.get(API_URL.format(key=tools.get_auth_key("league",
                                                                   "files/apikeys_private.txt"),
                                            name=SUMMONER_NAME))
SUMMONER_DATA = SUMMONER_DATA.json()

CONF_DATA["leage_id"] = SUMMONER_DATA[SUMMONER_NAME]["id"]

with open("files/configuration.conf", "w") as conf_file:
    for item in CONF_DATA:
        conf_file.write("{key} == {value}\n".format(key=item, value=CONF_DATA[item]))
