"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

import Tkinter as tk
import os
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

    options_panel = tk.Frame(window, bg="#000000")
    options_panel.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    options_panel.columnconfigure(0, weight=1)
    options_panel.rowconfigure(0, weight=1)

    image_path = os.path.abspath("files/gear.gif")
    options_icon = tk.PhotoImage(file=image_path)
    options_icon = options_icon.subsample(12, 12)  # Roughly 512 / 50

    options_button = tk.Button(options_panel, image=options_icon, bg="#000000", highlightbackground="#000000")
    options_button.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    # ########################################################################

    service_panel = tk.Frame(window, bg="#000000")
    service_panel.grid(column=0, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

    service_panel.rowconfigure(0, weight=1)
    service_panel.columnconfigure(0, weight=1)
    service_panel.rowconfigure(1, weight=0)

    image_path = os.path.abspath("files/steam.gif")
    steam_icon = tk.PhotoImage(file=image_path)
    steam_icon = steam_icon.subsample(24, 24)  # Roughly 1024 / 50

    steam_button = tk.Button(service_panel, image=steam_icon, bg="#000000", highlightbackground="#000000")
    steam_button.grid(column=0, row=0, sticky=tk.N+tk.W+tk.E)

    add_button = tk.Button(service_panel, text="+", bg="#000000", highlightbackground="#000000")
    add_button.grid(column=0, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

    # ########################################################################

    sort_panel = tk.Frame(window, bg="#1A324C")
    sort_panel.grid(column=1, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    sort_panel.rowconfigure(0, weight=1)
    sort_panel.columnconfigure(1, weight=1)
    sort_panel.columnconfigure(2, weight=1)

    sort_label = tk.Label(sort_panel, text="Sort by:", bg="#1A324C", fg="#FFFFFF")
    sort_label.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    app_sort_button = tk.Button(sort_panel, text="Application", bg="#1A324C", highlightbackground="#1A324C")
    app_sort_button.grid(column=1, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    person_sort_button = tk.Button(sort_panel, text="Person", bg="#1A324C", highlightbackground="#1A324C")
    person_sort_button.grid(column=2, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

    # ########################################################################

    # view_panel = tk.Frame(window, bg="#808080")
    # view_panel.grid(column=1, row=1, sticky=tk.N+tk.S+tk.E+tk.W)
    view_list = tk.Listbox(window, selectmode=tk.BROWSE, bg="#808080")
    view_list.grid(column=1, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

    status_list = steam.get_all_friend_statuses("2F74399CD94CA945FA648A0C1B911DB6", "76561198041498934")

    for friend in status_list:
        string = "{0} ({1})".format(friend[0], friend[2])
        view_list.insert(tk.END, string)

    # ########################################################################`

    window.mainloop()
