"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

import ast

def get_auth_key(service_name, file_path):
    """Get the Auth key of a certain API from a file"""
    # Fill a list with the lines from the Authkeys file this ...
    # ... allows it to be iterated through easy later on
    keys = []
    with open(file_path, 'r') as authfile:
        for line in authfile:
            keys.append(line)
    # Iterate through each line and look for the correct service ...
    # ... return the key (next line) when found
    for X in range(0, len(keys)):
        if service_name.lower() in keys[X].lower():
            # print keys[X+1].strip()
            return keys[X+1].strip()

def sort_by_person(input_status_dict):
    """Gets a dict of statuses and sorts them by an assigned name"""
    friend_map = {}
    with open("./files/friend_map.txt", "r") as map_file:
        for line in map_file:
            data = line.split("=")
            friend_map[data[0].strip()] = ast.literal_eval(data[1].strip())

    output_list = {}
    for friend in friend_map:
        output_list[friend] = {}
        for service in input_status_dict:
            for user in input_status_dict[service]:
                if user[1] in friend_map[friend][service]:
                    output_list[friend][service] = user
                else:
                    # TODO: Find a way to get the unassigned people together
                    pass
    return output_list
