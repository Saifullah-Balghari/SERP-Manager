import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox

from ..settings import *
from ..helpers import accounts

bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

class CurrentAccount(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Toplevel - Your Profile")
        self.geometry("400x320")
        self.resizable(False, False)
        self.configure(fg_color=bg) 

        # reading the current account information
        with open(current_role_path, 'r') as f:
                text = f.read()        
                username, password = text.split()

        account = accounts.get_account(username, password)
        self.username = account['username']
        self.password = account['password']
        self.role = account['role']
        self.created_at = account['created_at']

        self.widget()

    def widget(self):

        main_frame = ctk.CTkFrame(self, fg_color=bg, corner_radius=0)
        main_frame.pack(fill="both", expand=True, padx=0, pady=0)

        self.acc_icon = Image.open(acc_icon_path).resize((80, 80), Image.LANCZOS)
        self.acc_icon_photo = ImageTk.PhotoImage(self.acc_icon)

        self.acc_icon = ctk.CTkLabel(
            main_frame,
            image=self.acc_icon_photo,
            text=""
        )
        self.acc_icon.pack(fill="x", side="top", pady=5)

        self.username_label = ctk.CTkLabel(
            main_frame,
            text=self.username.title(),
            text_color=text_fg,
            font=("Helvetica", 22),
        )
        self.username_label.pack(fill="x", side="top", pady=2)

        # Details
        self.details_frame = ctk.CTkFrame(self, fg_color=fg)
        self.details_frame.pack(expand="true",fill="both", padx=20, side="top", pady=20, ipady=30, ipadx=30)

        # User name     
        self.user_name_label = ctk.CTkLabel(
            self.details_frame,
            text=f"Username: {self.username}",
            text_color=text_fg,
            anchor="w",
            font=("Helvetica", 14)
        )
        self.user_name_label.pack(fill="x", pady=5, padx=20)

        # Password
        self.user_name_label = ctk.CTkLabel(
            self.details_frame,
            text=f"Password: {self.password}",
            text_color=text_fg,
            anchor="w",
            font=("Helvetica", 14)
        )
        self.user_name_label.pack(fill="x", pady=5, padx=20)

        # Role
        self.role_label = ctk.CTkLabel(
            self.details_frame,
            text=f"Role: {self.role}",
            text_color=text_fg,
            anchor="w",
            font=("Helvetica", 14)
        )
        self.role_label.pack(fill="x", pady=5, padx=20)

        # DateCreated
        self.date_created_label = ctk.CTkLabel(
            self.details_frame,
            text=f"Date Created: {self.created_at}",
            text_color=text_fg,
            anchor="w",
            font=("Helvetica", 14)
        )
        self.date_created_label.pack(fill="x", pady=5, padx=20)

