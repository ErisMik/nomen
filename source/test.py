"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

import requests
import json

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
MYUSERID = "76561198041498934"

def get_username(steamid):
	# TODO: Make all the requests at a single time
	r = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={0}&steamids={1}".format(API_KEY, steamid))
	jo = r.json()
	user_dict = jo["response"]["players"][0]
	status = "Offline/Away"
	# TODO: Check if profile is set to private
	if user_dict["personastate"] == 1:
		status = "Online"
	return user_dict["personaname"] + " (" + status + ")"

response = requests.get("http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={0}&steamid={1}&relationship=friend".format(API_KEY, MYUSERID))
jsonObject = response.json()
friend_array = jsonObject["friendslist"]["friends"]

for friend in friend_array:
	print friend["steamid"] + " = " + get_username(friend["steamid"])
