from tkinter import messagebox

from src.login_win import LoginGui
from src.main_gui import SERPManagerGUI


role = LoginGui.get_role()

def login() -> bool:
    try:
        login_window = LoginGui()
        return login_window.signin()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"Failed to start the login window: {e}")
        return False
    
def main() -> None:
    if login():
        try:
            SERPManagerGUI( role)
        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"Failed to start the application: {e}")


if __name__ == "__main__":
    main()