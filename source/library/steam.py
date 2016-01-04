"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

import requests

GET_PLAYER_SUMMERIES_URL = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={steamid}"
GET_FRIENDS_LIST_URL = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={key}&steamid={steamid}&relationship={relation}"

def get_persona_from_id(api_key, steam_id):
    """Returns the username of a steam user from his steamid"""
    api_data = requests.get(GET_PLAYER_SUMMERIES_URL.format(key=api_key, steamid=steam_id))
    api_data_json = api_data.json()
    user_dictionary = api_data_json["response"]["players"][0]
    return user_dictionary["personaname"]

def get_status_from_id(api_key, steam_id):
    """Returns the status of a steam user from his steamid"""
    api_data = requests.get(GET_PLAYER_SUMMERIES_URL.format(key=api_key, steamid=steam_id))
    api_data_json = api_data.json()
    user_dictionary = api_data_json["response"]["players"][0]

    status = "Unknown"
    api_status = user_dictionary["personastate"]
    if api_status == 0:
        status = "Offline"
    elif api_status == 0 and user_dictionary["communityvisibilitystate"] == 1:
        status = "Private"
    elif api_status == 1:
        status = "Online"
    elif api_status == 2:
        status = "Busy"
    elif api_status == 3:
        status = "Away"
    elif api_status == 4:
        status = "Snooze"
    elif api_status == 5:
        status = "Looking to Trade"
    elif api_status == 6:
        status = "Looking to Play"
    return status

def get_all_friend_statuses(api_key, steam_id):
    """Returns the statuses of all a steam users's (steam_id) friend"""
    api_data = requests.get(GET_FRIENDS_LIST_URL.format(key=api_key,
                                                        steamid=steam_id, relation="friend"))
    api_data_json = api_data.json()
    print api_data_json
    friends_list = api_data_json["friendslist"]["friends"]

    # TODO: Make all the requests at a single time
    output_friends_list = []
    for friend in friends_list:
        friend_id = friend["steamid"]
        user = {get_persona_from_id(api_key, friend_id),
                friend_id,
                get_status_from_id(api_key, friend_id)}
        print "{0} ({1}) : {2}".format(user[0], user[1], user[2])
        output_friends_list.append(user)
    return output_friends_list
