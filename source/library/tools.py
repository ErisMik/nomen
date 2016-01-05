"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

def get_auth_key(service_name, file_path):
    """Get the Auth key of a certain API from a file"""
    # Fill a list with the lines from the Authkeys file
    keys = []
    with open(file_path, 'r') as authfile:
        for line in authfile:
            keys.append(line)
    # Iterate through each line and look for the correct service, return the key when found
    for X in range(0, len(keys)):
        if service_name.lower() in keys[X].lower():
            print keys[X+1].strip()
            return keys[X+1].strip()
