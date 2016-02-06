"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

import Tkinter as tk
import os
import thread
import time
import plugins.steam as steam
import plugins.league as league
import library.tools as tools

class AppWindow(tk.Frame):
    """Class that defines the main view window of the application"""
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure_frame()  # Configure the window frame

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
        self.columnconfigure(1, minsize=200, weight=1)
        self.rowconfigure(0, minsize=50, weight=0)
        self.rowconfigure(1, minsize=200, weight=1)

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
        # Create the panel and stickie it to the full grid cell
        self.service_panel = tk.Frame(self, bg=bg_colour)
        self.service_panel.grid(column=0, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

        # Configure the grid weights
        self.service_panel.rowconfigure(0, weight=1)
        self.service_panel.columnconfigure(0, weight=1)
        self.service_panel.rowconfigure(1, weight=0)

        # Process the image icons
        image_path = os.path.abspath("files/steam.gif")
        self.steam_icon = tk.PhotoImage(file=image_path)
        self.steam_icon = self.steam_icon.subsample(24, 24)  # Roughly 1024 / 50

        # image_path = os.path.abspath("files/league.gif")
        # self.league_icon = tk.PhotoImage(file=image_path)
        # self.league_icon = self.league_icon.subsample(24, 24)  # Roughly 1024 / 50

        # Create the button and add it to the grid
        self.steam_button = tk.Button(self.service_panel, image=self.steam_icon,
                                      bg=bg_colour, highlightbackground=bg_colour)
        self.steam_button.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E)

        # self.steam_button = tk.Button(self.service_panel, image=self.league_icon,
        #                               bg=bg_colour, highlightbackground=bg_colour)
        # self.steam_button.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E)

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
                                         bg=bg_colour, highlightbackground=bg_colour)
        self.app_sort_button.grid(column=1, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

        # Create the button and add it to the grid
        self.person_sort_button = tk.Button(self.sort_panel, text="Person",
                                            bg=bg_colour, highlightbackground=bg_colour)
        self.person_sort_button.grid(column=2, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    def view_list_widget(self, bg_colour="#808080"):
        """Method that creates, configures and fills the view-list widget"""
        # Create the listbox and stickie it to the full grid cell
        self.view_list = tk.Listbox(self, selectmode=tk.BROWSE, bg=bg_colour)
        self.view_list.grid(column=1, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

    def update_statuses(self, current_data):
        """Updates the list box (self.view_list) with the current entries"""
        # Sort the data alphanumerically
        current_data["steam"] = sorted(current_data["steam"])
        current_data["league"] = sorted(current_data["league"])

        self.view_list.delete(0, tk.END)  # Clear the list of it's entries

        self.view_list.insert(tk.END, "------------------------ Steam ----------------------")
        for friend in current_data["steam"]:
            string = "{0} ({1})".format(friend[0], friend[2])
            self.view_list.insert(tk.END, string)
        print "Steam Updated"

        self.view_list.insert(tk.END, "------------------ League of Legends ----------------")
        for friend in current_data["league"]:
            string = "{0} ({1})".format(friend[0], friend[2])
            self.view_list.insert(tk.END, string)
        print "League Updated"

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
        # Create a root window and add the application window as it's child
        self.root = tk.Tk()
        self.main_window = AppWindow(self.root)  # Create the ain window
        self.main_window.pack(side="top", fill="both", expand=True)  # Add it to the root frame

        # module_names = ["plugins.steam", "plugins.league"]
        # app_modules = map(__import__, module_names)
        # print app_modules

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

            steam_id_temp = "76561198041498934"
            league_id_temp = "36402541"

            # Get the statuses from Steam
            steam_auth_key = tools.get_auth_key("steam", "files/apikeys_private.txt")
            all_status_list["steam"] = steam.get_all_friend_statuses(steam_auth_key,
                                                                     steam_id_temp)

            # Get the statuses from League of Legends
            league_auth_key = tools.get_auth_key("league", "files/apikeys_private.txt")
            all_status_list["league"] = league.get_all_friend_statuses(league_auth_key,
                                                                       league_id_temp)

            # Add the statuses to the window, then create a job to do this again in 10 seconds
            self.main_window.update_statuses(all_status_list)
            time.sleep(delay)
