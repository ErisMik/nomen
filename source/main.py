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
        self.createWidgets()
        # self.columnconfigure(0, minsize=500)
        # self.rowconfigure(0, minsize=500)

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid(column=0, row=0, sticky=tk.N+tk.S+tk.E+tk.W)

        self.addButton = tk.Button(self, text='Add',
            command=self.quit)
        self.addButton.grid(column=1, row=1)

# ############################################################################
# Main method
if __name__ == "__main__":
    print "works"
    app = Application()
    app.master.title('Sample application')
    app.mainloop()
