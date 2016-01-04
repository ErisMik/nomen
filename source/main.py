"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

# Imports
import Tkinter as tk

# ############################################################################
# Graphical Application class
class Application(tk.Frame):
    """ Class that creates the GUI """
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.create_widgets()
        # self.columnconfigure(0, minsize=500)
        # self.rowconfigure(0, minsize=500)

    def create_widgets(self):
        """ TODO """
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.quit_button = tk.Button(self, text='Quit',
                                     command=self.quit)
        self.quit_button.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

        self.add_button = tk.Button(self, text='Add',
                                    command=self.quit)
        self.add_button.grid(column=1, row=1)

# ############################################################################
# Main method
if __name__ == "__main__":
    print "works"
    APP = Application()
    APP.master.title('Sample application')
    APP.mainloop()
