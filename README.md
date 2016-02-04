Notify-Me
=========
Program for my Computer Science IA

### Description
Acts as a hub for online statuses. It grabs them from their respective APIs and shows them in a graphical interface.

### Language
Python 2.7

### External Resources
##### APIs:
- Steam
- Skype
- League of Legends
- Facebook
- Slack + Hipchat
- Guild Wars 2

##### Libraries:
- Python default library
	- Tkinter (Graphics Library)
	- json (JSON parsing library)
	- os (Give OS tools)
- PIP libraries
	- requests (HTTP requests Library)
- Other libraries (link)
	- N/A

### Licensing
I'm not actually sure

### Limitations
- League: Can't get friends list, worked around by finding players that a user often plays with, and determines if the are in a gmae or played recently

### Library Reference
##### Steam
- get_data_from_ids(api_key, steam_ids)
	- Function
    - """Gets the full dictionary of multiple users"""
- get_persona_from_id(api_key, steam_id)
	- Function
	- """Returns the username of a steam user from his steamid"""
- get_status_from_id(api_key, steam_id)
	- Function
	- """Returns the status of a steam user from his steamid"""
- def get_status_from_data(data)
	- Function
    - """Returns the status of a steam user given the user data dictionary"""
- get_all_friend_statuses(api_key, steam_id)
	- Function
	- """Returns the statuses of all a steam users's (steam_id) friend"""

#### League of Legends
- get_friends_from_id(api_key, summoner_id)
	- Function
	- """Determine the friends of a user by looking at recent games, then returns the friends data"""
- get_friends_from_file(file_path)
	- Function
	- """Gets a list of friends from a file"""
- get_data_from_id(api_key, friend_list)
	- Function
	- """Get the summoner data from a list of friend ids"""
- test_for_current_game(api_key, summoner_id)
	- Function
	- """Returns a string that is the current status of a user"""
- test_for_recent_game(api_key, summoner_id)
	- Function
	- """Returns a string that is the current status of a user"""
- get_all_friend_statuses(api_key, summoner_id)
	- Function
	- """Returns the statuses of all a league of legends user's friends"""

##### Tools
- get_auth_key(service_name, file_path):
	- Function
	- """Get the Auth key of a certain API from a file"""

##### Graphics
- AppWindow(tk.Frame)
	- Class
- OptionWindow()
	- Class
- AppManager()
	- Class

### Other Refrence
steam_id = "76561198041498934"
summoner_id = "36402541"
