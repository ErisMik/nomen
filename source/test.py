"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

import Tkinter as tk
from library import steam

# print "Everything working as of now!"

# ############################################################################
# Main method
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Testing Window")
    window.configure(background="#999999")

    window.columnconfigure(0, minsize=50, weight=0)
    window.columnconfigure(1, minsize=200, weight=1)

    window.rowconfigure(0, minsize=50, weight=0)
    window.rowconfigure(1, minsize=200, weight=1)

    # ########################################################################

    options_panel = tk.Frame(window, bg="#AA55f7")
    options_panel.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    options_panel.columnconfigure(0, weight=1)
    options_panel.rowconfigure(0, weight=1)

    options_button = tk.Button(options_panel, text="Opt", bg="#AA55f7", highlightbackground="#AA55f7")
    options_button.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    # ########################################################################

    service_panel = tk.Frame(window, bg="#000000")
    service_panel.grid(column=0, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

    service_panel.rowconfigure(0, weight=1)
    service_panel.columnconfigure(0, weight=1)
    service_panel.rowconfigure(1, weight=0)

    add_button = tk.Button(service_panel, text="+", bg="#000000", highlightbackground="#000000")
    add_button.grid(column=0, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

    # ########################################################################

    sort_panel = tk.Frame(window, bg="#990066")
    sort_panel.grid(column=1, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    sort_panel.rowconfigure(0, weight=1)
    sort_panel.columnconfigure(1, weight=1)
    sort_panel.columnconfigure(2, weight=1)

    sort_label = tk.Label(sort_panel, text="Sort by:", bg="#990066")
    sort_label.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    app_sort_button = tk.Button(sort_panel, text="Application", bg="#990066", highlightbackground="#990066")
    app_sort_button.grid(column=1, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    person_sort_button = tk.Button(sort_panel, text="Person", bg="#990066", highlightbackground="#990066")
    person_sort_button.grid(column=2, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    # ########################################################################

    view_panel = tk.Frame(window, bg="#55ffaa")
    view_panel.grid(column=1, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

    status_list = steam.get_all_friend_statuses("", "76561198041498934")

    for friend in status_list:
        string = "Name: {0} Status: {1}".format(friend[0], friend[2])
        print string
        new_pan = tk.Label(view_panel, text=string, bg="#55ffaa")
        new_pan.grid(column=0, sticky=tk.E+tk.W)

    # ########################################################################`

    window.mainloop()
