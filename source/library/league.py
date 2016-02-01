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
GET_CURRENT_GAME_URL = ("https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/{summonid}"+
                        "?api_key={key}")

def get_friends_from_id(api_key, summoner_id):
    """Determine the friends of a user by looking at recent games, then returns the friends data"""
    all_recent_games = requests.get(GET_RECENT_GAMES_URL.format(key=api_key, summonid=summoner_id))
    all_recent_games_json = all_recent_games.json()
    all_fellow_players = []
    for game in all_recent_games_json["games"]:
        if "fellowPlayers" in game:
            for fellow_player in game["fellowPlayers"]:
                all_fellow_players.append(fellow_player["summonerId"])

    # TODO: Extremely iniffecient, replace soon
    all_friends = [item for item, count in collections.Counter(all_fellow_players).items() if count > 1]
    for x in range(0, len(all_friends)):
        all_friends[x] = str(all_friends[x])

    return all_friends

def get_friends_from_file(file_path):
    """Gets a list of friends from a file"""
    # TODO: The actual code
    return

def get_data_from_id(api_key, friend_list):
    """Get the summoner data from a list of friend ids"""
    formatted_friend_list = ",".join(friend_list)

    all_friend_data = requests.get(GET_SUMMONER_DATA_URL.format(summonid=formatted_friend_list,
                                                                key=api_key))
    all_friend_data_json = all_friend_data.json()
    return all_friend_data_json

def test_for_current_game(api_key, summoner_id):
    """Returns a string that is the current status of a user"""
    current_game = requests.get(GET_CURRENT_GAME_URL.format(key=api_key, summonid=summoner_id))
    current_game_json = current_game.json()
    response = "Away"
    if "gameId" in current_game_json:
        response = "In game"
    return response

def test_for_recent_game(api_key, summoner_id):
    """Returns a string that is the current status of a user"""
    recent_games = requests.get(GET_RECENT_GAMES_URL.format(key=api_key, summonid=summoner_id))
    recent_games_json = recent_games.json()
    # Gather the data
    most_recent_game = recent_games_json["games"][0]
    start_time = most_recent_game["createDate"]  # Milliseconds since epoch (Asuming unix epoch)
    current_time = time.time()  # Seconds since epoch (Assuming Unix epoch)
    play_time = most_recent_game["stats"]["timePlayed"]  # In seconds

    # Do the Math
    start_time = start_time / 1000  # Convert to seconds
    end_time = start_time + play_time  # Find the end time of the game
    time_since = current_time - end_time  # Determine how long ago the game was
    time_since = time_since / 60  # Convert back to minutes

    response = "Offline"
    if time_since < 10:
        response = "Played {0} mins ago".format(int(time_since))

    return response

def get_all_friend_statuses(api_key, summoner_id):
    """Returns the statuses of all a league of legends user's friends"""
    # Determine friends (Played more than one games with)
    determined_friends = get_friends_from_id(api_key, summoner_id)

    # Read pre-set friends
    read_friends = get_friends_from_file("files/league_friends_private.txt")

    # Find summoner data
    all_friends = determined_friends
    if read_friends:
        all_friends += read_friends  # Merge the friend lists together
    friend_data = get_data_from_id(api_key, all_friends)

    # Are friends in game?
    for friend in friend_data:
        friend_data[friend]["status"] = test_for_current_game(api_key, friend)

    # Last Game friends played
    for friend in friend_data:
        new_status = test_for_recent_game(api_key, friend)
        if "In game" not in friend_data[friend]["status"]:
            friend_data[friend]["status"] = new_status

    # Print debug lines
    # for friend in friend_data:
    #     print friend_data[friend]["name"] + " - " + str(friend_data[friend]["id"]) + " - " + friend_data[friend]["status"]

    # Return statuses
    output_friends_list = []
    for friend in friend_data:
        user = [friend_data[friend]["name"],
                str(friend_data[friend]["id"]),
                friend_data[friend]["status"]]
        # print "{0} ({1}) : {2}".format(user[0], user[1], user[2])
        output_friends_list.append(user)
    return output_friends_list
