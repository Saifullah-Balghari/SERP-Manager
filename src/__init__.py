# Disclaimer:
# Icons are not designed by me, sourced from www.flaticon.com

# This is a simple GUI Application that can be used as an Examinations, Results and Paper Manager.
# As of now this project is a personal side project and is not intended for commercial use or distribution.

__version__ = "beta 1.0.0"

from . import login_win
from . import main_gui

root = login_win.LoginGui()
def login():
    root.mainloop()

    return root.verified

def main():
    if login():
        main_gui.SERPManagerGUI()
