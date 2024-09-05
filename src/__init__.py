from . import login_win
from . import main_gui

root = login_win.LoginGui()
def login():
    root.mainloop()

    return root.verified

def main():
    if login():
        main_gui.SERPManagerGUI()
    else:
        print("Login failed.")
        exit()
