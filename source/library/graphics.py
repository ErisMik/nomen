"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

import Tkinter as tk
import os
import thread
import time
import library.tools as tools

class AppWindow(tk.Frame):
    """Class that defines the main view window of the application"""
    # Gross call variables :/
    sort_by_service = True
    service_filter = {}

    def __init__(self, master, plugin_list):
        tk.Frame.__init__(self, master)
        self.configure_frame()  # Configure the window frame

        # Formulate the filter dictionary, set to true by default
        for plugin in plugin_list:
            AppWindow.service_filter[plugin] = True

        # Add the rest of the widgets
        self.option_panel_widget()
        self.service_panel_widget()
        self.sort_panel_widget()
        self.view_list_widget()

    def configure_frame(self):
        """Method that configures certain elements of the window"""
        # Prepare the window title and colour
        self.master.title("Computer Science IA")
        self.configure(background="#990099")

        # Prepare the columns and rows
        self.columnconfigure(0, minsize=50, weight=0)
        self.columnconfigure(1, minsize=250, weight=1)
        self.rowconfigure(0, minsize=50, weight=0)
        self.rowconfigure(1, minsize=400, weight=1)

    def option_panel_widget(self, bg_colour="#000000"):
        """Method that creates, configures and fills the options widget"""
        # Create the panel and stickie it to the full grid cell
        self.options_panel = tk.Frame(self, bg=bg_colour)
        self.options_panel.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

        # Configure the grid weights
        self.options_panel.columnconfigure(0, weight=1)
        self.options_panel.rowconfigure(0, weight=1)

        # Process the image icon
        image_path = os.path.abspath("files/gear.gif")
        self.options_icon = tk.PhotoImage(file=image_path)
        self.options_icon = self.options_icon.subsample(12, 12)  # Roughly 512 / 50

        # Create the button and add it to the grid
        self.options_button = tk.Button(self.options_panel, image=self.options_icon,
                                        bg=bg_colour, highlightbackground=bg_colour)
        self.options_button.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    def service_panel_widget(self, bg_colour="#000000"):
        """Method that creates, configures and fills the service widget"""
        # Create the whole panel and stickie it to the full grid cell
        self.service_panel = tk.Frame(self, bg=bg_colour)
        self.service_panel.grid(column=0, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Create the filter button panel
        self.filter_panel = tk.Frame(self.service_panel, bg=bg_colour)
        self.filter_panel.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

        # Configure the grid weights
        self.service_panel.rowconfigure(0, weight=1)
        self.service_panel.columnconfigure(0, weight=1)
        self.service_panel.rowconfigure(1, weight=0)

        # Process the image icons
        image_path = os.path.abspath("files/steam.gif")
        self.steam_icon = tk.PhotoImage(file=image_path)
        self.steam_icon = self.steam_icon.subsample(24, 24)  # Roughly 1024 / 50

        image_path = os.path.abspath("files/league.gif")
        self.league_icon = tk.PhotoImage(file=image_path)
        self.league_icon = self.league_icon.subsample(24, 24)  # Roughly 1024 / 50

        # Create the buttons and add it to the grid
        self.steam_button = tk.Button(self.filter_panel, image=self.steam_icon,
                                      bg=bg_colour, highlightbackground=bg_colour,
                                      command=lambda: self.toggle_filter("steam"))
        self.steam_button.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E)

        self.league_button = tk.Button(self.filter_panel, image=self.league_icon,
                                       bg=bg_colour, highlightbackground=bg_colour,
                                       command=lambda: self.toggle_filter("league"))
        self.league_button.grid(column=0, row=1, sticky=tk.N+tk.W+tk.E)

        # Create the button and add it to the grid
        self.add_button = tk.Button(self.service_panel, text="+",
                                    bg=bg_colour, highlightbackground=bg_colour)
        self.add_button.grid(column=0, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

    def sort_panel_widget(self, bg_colour="#1A324C", fg_colour="#FFFFFF"):
        """Method that creates, configures and fills the panel widget"""
        # Create the panel and stickie it to the full grid cell
        self.sort_panel = tk.Frame(self, bg=bg_colour)
        self.sort_panel.grid(column=1, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

        # Configure the grid weights
        self.sort_panel.rowconfigure(0, weight=1)
        self.sort_panel.columnconfigure(1, weight=1)
        self.sort_panel.columnconfigure(2, weight=1)

        # Create the label and add it to the grid
        self.sort_label = tk.Label(self.sort_panel, text=" Sort by:", bg=bg_colour, fg=fg_colour)
        self.sort_label.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

        # Create the button and add it to the grid
        self.app_sort_button = tk.Button(self.sort_panel, text="Application",
                                         bg=bg_colour, highlightbackground=bg_colour,
                                         command=lambda: self.toggle_sort_by(True))
        self.app_sort_button.grid(column=1, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

        # Create the button and add it to the grid
        self.person_sort_button = tk.Button(self.sort_panel, text="Person",
                                            bg=bg_colour, highlightbackground=bg_colour,
                                            command=lambda: self.toggle_sort_by(False))
        self.person_sort_button.grid(column=2, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    def view_list_widget(self, bg_colour="#808080"):
        """Method that creates, configures and fills the view-list widget"""
        # Create the listbox and stickie it to the full grid cell
        self.view_list = tk.Listbox(self, selectmode=tk.BROWSE, bg=bg_colour)
        self.view_list.grid(column=1, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

    def toggle_sort_by(self, new):
        """Sets the sort by boolean to a different boolean"""
        print "Sort by %s -> %s" % (AppWindow.sort_by_service, new)
        AppWindow.sort_by_service = new

    def toggle_filter(self, service):
        """Flips the boolean state of a service given it's name"""
        AppWindow.service_filter[service] = not AppWindow.service_filter[service]
        print "%s filter set to %s" % (service, AppWindow.service_filter[service])

    def update_statuses(self, current_data):
        """Updates the list box (self.view_list) with the current entries"""
        by_service = AppWindow.sort_by_service
        if by_service:
            # Sort the data alphanumerically
            for service in current_data:
                current_data[service] = sorted(current_data[service])

            self.view_list.delete(0, tk.END)  # Clear the list of it's entries

            # Print the statuses of every service here
            for service in current_data:
                if AppWindow.service_filter[service]:
                    self.view_list.insert(tk.END, "------------------------ %s ----------------------" % service.capitalize())
                    for friend in current_data[service]:
                        string = "{0} ({1})".format(friend[0], friend[2])
                        self.view_list.insert(tk.END, string)
                print "%s printed" % service
        else:
            # Sort the data according to the friend map
            current_data = tools.sort_by_person(current_data)

            self.view_list.delete(0, tk.END)  # Clear the list of it's entries

            for friend in current_data:
                self.view_list.insert(tk.END, "------------------------ %s ----------------------" % friend.capitalize())
                for service in current_data[friend]:
                    if AppWindow.service_filter[service]:
                        string = "{0} ({1})".format(current_data[friend][service][0], current_data[friend][service][2])
                        self.view_list.insert(tk.END, string)
                print "%s printed" % friend

        print "============== Update Cycle Finish =============="

class OptionWindow(tk.Frame):
    """Class that defines the options window of the application"""
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Options")
        self.configure(background="#990099")

        # Prepare the columns and rows
        self.columnconfigure(0, minsize=500, weight=1)
        self.rowconfigure(0, minsize=500, weight=1)

        # Add the options
        self.option_boxes()

    def option_boxes(self):
        self.c = tk.Checkbutton(self.master, text="This is a Test")
        self.c.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E)

class AppManager():
    """Class that manages the application and it's windows"""
    def __init__(self):
        # Read all the plugin names
        plugin_list = []
        for file_name in os.listdir("./plugins"):
            if file_name.endswith(".py") and "__init__" not in file_name:
                plugin_list.append(file_name.split(".")[0])

        # Import the plugins from the plugin names
        self.service_modules = {}
        for plugin_name in plugin_list:
            self.service_modules[plugin_name] = __import__("plugins.{0}".format(plugin_name), fromlist=["plugins"])

        # Create a root window and add the application window as it's child
        self.root = tk.Tk()
        self.main_window = AppWindow(self.root, plugin_list)  # Create the ain window
        self.main_window.pack(side="top", fill="both", expand=True)  # Add it to the root frame

        # Attempting to thread the update cycle
        try:
            thread.start_new_thread(self.update, ())
        except Exception as e:
            print("The thread done broke itself: ", e)

        self.root.mainloop()  # Start the application

    def update(self, delay=10):
        """Updates all the statuses and adds this call to the main loop"""
        while True:
            all_status_list = {}

            # TODO: Replace this with a function from library.tools 
            ids = {
                "steam" : "76561198041498934",
                "league" : "36402541"
            }

            # Get the statuses from every module
            for module in self.service_modules:
                print("%s next ..." % module)
                auth_key = tools.get_auth_key(module, "files/apikeys_private.txt")
                all_status_list[module] = self.service_modules[module].get_all_friend_statuses(auth_key,
                                                                     ids[module])
                print("... %s updated" % module)

            # Add the statuses to the window, then create a job to do this again in 10 seconds
            self.main_window.update_statuses(all_status_list)
            time.sleep(delay)
