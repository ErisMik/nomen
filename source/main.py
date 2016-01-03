"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""
# Imports
import Tkinter as tk

# Graphical Application class
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()

# Main method
if __name__ == "__main__":
    print "works"
    app = Application()
    app.master.title('Sample application')
    app.mainloop()
