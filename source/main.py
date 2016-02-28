"""
Eric Mikulin
Computer Science IB Internal Assement
Python 2.7
"""

from library import graphics
import os.path
import prepare

# Main method
if __name__ == "__main__":
    # TODO: Check for and install dependencies
    if not os.path.isfile("files/configuration.conf"):
        print "Configuration file not found!"
        prepare.main()

    APPLICATION = graphics.AppManager()  # Start the main application
