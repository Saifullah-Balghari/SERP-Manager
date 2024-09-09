from . import login_win
from . import main_gui
from .settings import *

import os

root = login_win.LoginGui()
def login():
    root.mainloop()

    return root.verified

def main():
    if login():
        main_gui.SERPManagerGUI()
