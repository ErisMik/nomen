Notify-Me
=========
Program for my Computer Science IA

### Description
Acts as a hub for online statuses

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
MIT License

### Library Reference
##### Steam
- get_persona_from_id(api_key, steam_id)
	- """Returns the username of a steam user from his steamid"""
- get_status_from_id(api_key, steam_id)
	- """Returns the status of a steam user from his steamid"""
- get_all_friend_statuses(api_key, steam_id)
	- """Returns the statuses of all a steam users's (steam_id) friend"""

##### Tools
- get_auth_key(service_name, file_path):
	- """Get the Auth key of a certain API from a file"""