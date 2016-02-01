"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

# Imports
import requests

# Constants
GET_PLAYER_SUMMERIES_URL = ("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"+
                            "?key={key}&steamids={steamid}")
GET_FRIENDS_LIST_URL = ("http://api.steampowered.com/ISteamUser/GetFriendList/v0001/"+
                        "?key={key}&steamid={steamid}&relationship={relation}")

def get_data_from_ids(api_key, steam_ids):
    """Gets the full dictionary of multiple users"""
    # Perform the API request
    ",".join(steam_ids)  # Convert the list into a string of ids separated by commas
    api_data = requests.get(GET_PLAYER_SUMMERIES_URL.format(key=api_key, steamid=steam_ids))
    api_data_json = api_data.json()
    user_list = []
    # Convert the JSON into a list of dictionaries
    for user in api_data_json["response"]["players"]:
        user_list.append(user)
    return user_list

def get_persona_from_id(api_key, steam_id):
    """Returns the username of a steam user from his steamid"""
    # Perform the API request
    api_data = requests.get(GET_PLAYER_SUMMERIES_URL.format(key=api_key, steamid=steam_id))
    api_data_json = api_data.json()
    user_dictionary = api_data_json["response"]["players"][0]  # Grab the inner data
    return user_dictionary["personaname"]

def get_status_from_id(api_key, steam_id):
    """Returns the status of a steam user from his steamid"""
    # Perform the API request
    api_data = requests.get(GET_PLAYER_SUMMERIES_URL.format(key=api_key, steamid=steam_id))
    api_data_json = api_data.json()
    user_dictionary = api_data_json["response"]["players"][0]  # Grab the inner data
    return get_status_from_data(user_dictionary)

def get_status_from_data(data):
    """Returns the status of a steam user given the user data dictionary"""
    # Determine the status of the user
    status = "Unknown"
    api_status = data["personastate"]
    # Check if the user profile is set to private
    if api_status == 0 and data["communityvisibilitystate"] == 1:
        status = "Private"
    # Check for the other statuses
    elif api_status == 0:
        status = "Offline"
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
    # Perform the API request
    api_data = requests.get(GET_FRIENDS_LIST_URL.format(key=api_key,
                                                        steamid=steam_id, relation="friend"))
    api_data_json = api_data.json()
    # print api_data_json
    friends_list = api_data_json["friendslist"]["friends"]  # Grab the inner data

    # For every friend, retrieve just the steam_id and add it to a list
    friend_ids_list = []
    for friend in friends_list:
        friend_id = friend["steamid"]
        friend_ids_list.append(friend_id)

    # Get the data form the list of ids
    friends_data = get_data_from_ids(api_key, friend_ids_list)

    # Create the list of output strings using the data retrieved earlier
    output_friends_list = []
    for friend in friends_data:
        user = [friend["personaname"],
                friend["steamid"],
                get_status_from_data(friend)]
        # print "{0} ({1}) : {2}".format(user[0], user[1], user[2])
        output_friends_list.append(user)
    return output_friends_list
