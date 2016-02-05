"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

# Imports
import requests
import time
import collections

# Constants
GET_RECENT_GAMES_URL = ("https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/{summonid}/recent"+
                        "?api_key={key}")
GET_SUMMONER_DATA_URL = ("https://na.api.pvp.net/api/lol/na/v1.4/summoner/{summonid}"+
                         "?api_key={key}")
GET_SUMMONER_ID_URL = ("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/{name}"+
                       "?api_key={key}")
GET_CURRENT_GAME_URL = ("https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/{summonid}"+
                        "?api_key={key}")

def get_friends_from_id(api_key, summoner_id):
    """Determine the friends of a user by looking at recent games, then returns the friends data"""
    all_recent_games = requests.get(GET_RECENT_GAMES_URL.format(key=api_key, summonid=summoner_id))
    all_recent_games_json = all_recent_games.json()
    all_fellow_players = []
    # Find all the players the user has played with in thier recent games
    for game in all_recent_games_json["games"]:
        if "fellowPlayers" in game:
            for fellow_player in game["fellowPlayers"]:
                all_fellow_players.append(fellow_player["summonerId"])

    # Find duplicates and keep them because they're assumed friends
    # TODO: Extremely iniffecient, replace soon
    all_friends = [item for item, count in collections.Counter(all_fellow_players).items() if count > 1]
    for x in range(0, len(all_friends)):
        all_friends[x] = str(all_friends[x])

    return all_friends

def get_id_from_name(api_key, summoner_name):
    """Gets the summoner id form the summoner name"""
    summoner_data = requests.get(GET_SUMMONER_ID_URL.format(key=api_key, name=summoner_name))
    summoner_data = summoner_data.json()
    return summoner_data[summoner_name]["id"]

def get_friends_from_file(api_key, file_path):
    """Gets a list of friends from a file"""
    # Read all the lines and store them into a list
    all_friends = []
    with open(file_path, 'r') as f_file:
        for line in f_file:
            all_friends.append(line.strip())
    # For each line, read the summoner_id or api call for it
    for friend in range(0, len(all_friends)):
        data = all_friends.pop(friend).split("=")  # Split the key value pairs
        # Strip out all the whitespace
        for item in range(0, len(data)):
            data[item] = data[item].strip()
        # If the ID is not known, make an API call for it
        # Else use the one written in the file
        if "?" in data[1]:
            data[1] = "="
            data.append(str(get_id_from_name(api_key, data[0])))
        else:
            data.append(data[1])
            data[1] = "="
        data.append("\n")
        all_friends.insert(0, " ".join(data))
    # Write all the lines back into the file, this way the unknown ids are written in
    with open(file_path, "w") as f_file:
        for data in all_friends:
            f_file.write(data)

    # Format the data to be returned
    output_data = []
    for friend in all_friends:
        output_data.append(str(friend.split("=")[1].strip()))
    return output_data  # Return data

def get_data_from_id(api_key, friend_list):
    """Get the summoner data from a list of friend ids"""
    formatted_friend_list = ",".join(friend_list)  # Format the names to be put into the API request
    all_friend_data = requests.get(GET_SUMMONER_DATA_URL.format(summonid=formatted_friend_list,
                                                                key=api_key))
    all_friend_data_json = all_friend_data.json()
    return all_friend_data_json

def test_for_current_game(api_key, summoner_id):
    """Returns a string that is the current status of a user"""
    current_game = requests.get(GET_CURRENT_GAME_URL.format(key=api_key, summonid=summoner_id))
    current_game_json = current_game.json()
    response = "Away"
    if "gameId" in current_game_json:  # If the current game returns a game (instead of 404)
        response = "In game"  # Set status appropriately
    return response

def test_for_recent_game(api_key, summoner_id):
    """Returns a string that is the current status of a user"""
    recent_games = requests.get(GET_RECENT_GAMES_URL.format(key=api_key, summonid=summoner_id))
    recent_games_json = recent_games.json()
    # Gather the data
    most_recent_game = recent_games_json["games"][0]
    start_time = most_recent_game["createDate"] * 0.001  # Milliseconds since epoch (Asuming unix epoch)
    # print "start in ms: " + str(start_time)
    current_time = time.time()  # Seconds since epoch (Assuming Unix epoch)
    # print "current in s: " + str(current_time)
    play_time = most_recent_game["stats"]["timePlayed"]  # In seconds
    # print "play tim in s: " + str(play_time)

    # Do the Math
    # TODO: Something causes the math to be a few minutes off, need to investigate
    # start_time = start_time * 0.001  # Convert to seconds
    # print "start in s: " + str(start_time)
    end_time = start_time + play_time  # Find the end time of the game
    # print "end in s: " + str(end_time)
    time_since = current_time - end_time  # Determine how long ago the game was
    # print "time since in s: " + str(time_since)
    time_since = time_since / 60  # Convert to minutes
    # print "time since in m: " + str(time_since)
    # print "=========="

    # Determine what status to return to the user
    response = "Offline"
    if time_since < 10:
        response = "Played {0} mins ago".format(int(time_since))
    elif time_since < 15:
        response = "Away"

    return response

def get_all_friend_statuses(api_key, summoner_id):
    """Returns the statuses of all a league of legends user's friends"""
    # Determine friends (Played more than one games with recently)
    determined_friends = get_friends_from_id(api_key, summoner_id)

    # Read pre-set friends from a file
    read_friends = get_friends_from_file(api_key, "files/league_friends_private.txt")

    # Merge the two friends lists together
    all_friends = determined_friends
    if read_friends:
        all_friends += read_friends

    # Get the friend data from the friend summoner ids
    friend_data = get_data_from_id(api_key, all_friends)

    # Check if the friends are currently in game, and set status
    for friend in friend_data:
        friend_data[friend]["status"] = test_for_current_game(api_key, friend)

    # Check the friends most recent game, and set status based on that
    for friend in friend_data:
        # TODO: Make the delay as efficient as possible
        time.sleep(5)  # This is a quick and dirty way to prevent me from breaching the 10 api calls per 10 seconds rule
        new_status = test_for_recent_game(api_key, friend)
        if "In game" not in friend_data[friend]["status"]:
            friend_data[friend]["status"] = new_status

    # Print debug lines
    # for friend in friend_data:
    #     print friend_data[friend]["name"] + " - " + str(friend_data[friend]["id"]) + " - " + friend_data[friend]["status"]

    # Convert to standard data format and the return
    output_friends_list = []
    for friend in friend_data:
        user = [friend_data[friend]["name"],
                str(friend_data[friend]["id"]),
                friend_data[friend]["status"]]
        # print "{0} ({1}) : {2}".format(user[0], user[1], user[2])
        output_friends_list.append(user)
    return output_friends_list
