"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

import webbrowser
import requests
from library import tools

configuration_data = {}

# Determine steam id
know_steam = raw_input("Do you know your steam id number? (yes or no): ")
if "n" in know_steam:
	webbrowser.open("http://steamidfinder.com/", new=1)
	webbrowser.open("https://store.steampowered.com//login/?redir=0", new=1)
configuration_data["steam_id"] = raw_input("What is your steamid64 number?")

# Detrmine league id
summoner_name = raw_input("What is your league summoner name?")
# TODO: shorten line
summoner_data = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{name}?api_key={key}".format(key=tools.get_auth_key("league", "files/apikeys_private.txt"), name=summoner_name))
summoner_data = summoner_data.json()

configuration_data["leage_id"] = summoner_data[summoner_name]["id"]

with open("files/configuration.conf", "w") as conf_file:
	for item in configuration_data:
		conf_file.write("{key} == {value}\n".format(key=item, value=configuration_data[item]))
