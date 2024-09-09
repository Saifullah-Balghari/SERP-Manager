import customtkinter as ctk
from PIL import Image, ImageTk

from .settings import *

bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

class CurrentAccount(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("")
        self.resizable(False, False)

        with open(current_role_path, 'r') as f:
                text = f.read()        
                self.username, self.role = text.split()

        self.widget()

    def widget(self):

        main_frame = ctk.CTkFrame(self, fg_color=bg, corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        self.acc_icon = Image.open(acc_icon_path).resize((200, 200), Image.LANCZOS)
        self.acc_icon_photo = ImageTk.PhotoImage(self.acc_icon)

        self.acc_icon_label = ctk.CTkLabel(
            main_frame,
            image=self.acc_icon_photo,
            text=""
        )
        self.acc_icon_label.grid(pady=20, padx=10, row=0, column=0, rowspan=8, sticky="nsew")

        self.login_label = ctk.CTkLabel(
            main_frame,
            text="Current Account",
            text_color=text_fg,
            anchor="center",
            font=("Helvetica", 26, "bold")
        )
        self.login_label.grid(pady=10, padx=10, row=0, column=1, columnspan=2, sticky="nsew")

        self.username_label = ctk.CTkLabel(
            main_frame,
            text=f"Username: \t {self.username} ",
            text_color=text_fg,
            anchor="w",
            font=("Helvetica", 18)
        )
        self.username_label.grid(pady=(5, 0), padx=20, row=1, column=1, columnspan=2, sticky="ew")

        self.role = ctk.CTkLabel(
            main_frame,
            text_color=text_fg,
            text=f"Role:     \t\t {self.role}",
            anchor="w",
            font=("Helvetica", 18)
        )
        self.role.grid(pady=(5, 0), padx=20, row=3, column=1, columnspan=2, sticky="ew")
    
        self.delete_button = ctk.CTkButton(
            main_frame,
            text="Delete Profile",
            text_color=fg,
            font=("Helvetica", 18, "bold"),
            command=None,
            hover_color=btn_hvr,
            fg_color=btn_active
        )
        self.delete_button.grid(pady=20, padx=(20, 5), row=7, column=1)

        self.close_button = ctk.CTkButton(
            main_frame,
            text="Close",
            text_color=text_fg_2,
            font=("Helvetica", 18, "bold"),
            command=self.destroy,
            hover_color=btn_hvr,
            fg_color=btn_active
        )
        self.close_button.grid(pady=20, padx=(5, 20), row=7, column=2)
