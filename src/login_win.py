from PIL import Image
import customtkinter as ctk

from .settings import *
from .helpers import accounts
from .components import messagebox

ctk.set_appearance_mode("light")

bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"
btn_active_2 = "#E9D7FE"

class LoginGui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login Menu")

        self.side_img = CTkImage(Image.open(side_icon_path), size=(300, 480))
        self.name_icon = CTkImage(Image.open(name_icon_path), size=(20,20))
        self.password_icon = CTkImage(Image.open(password_icon_path), size=(18,18))                     

        self.login_frame = ctk.CTkFrame(self, fg_color="#FFF", corner_radius=0)
        self.login_frame.grid(sticky="nsew")

        self.login()

    def login(self):

        for widget in self.login_frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(master=self.login_frame, text="", image=self.side_img).pack(expand=True, side="left")

        frame = ctk.CTkFrame(master=self.login_frame, width=300, height=480, fg_color=bg)
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        ctk.CTkLabel(
            master=frame, 
            text="Welcome Back!", 
            text_color=text_fg, 
            anchor="w", 
            justify="left", 
            font=("Helvetica", 24)          
        ).pack(anchor="w", pady=(50, 5), padx=(25, 0))

        ctk.CTkLabel(
            master=frame, 
            text="Sign in to your account", 
            text_color="#7E7E7E", 
            anchor="w", 
            justify="left", 
            font=("Helvetica", 12)
        ).pack(anchor="w", padx=(25, 0))

        ctk.CTkLabel(
            master=frame, 
            text="  Username:", 
            text_color=text_fg, 
            anchor="w", 
            justify="left", 
            font=("Helvetica", 14), 
            image=self.name_icon, 
            compound="left"
        ).pack(anchor="w", pady=(38, 0), padx=(25, 0))

        self.username_entry = ctk.CTkEntry(
            master=frame, 
            width=225, 
            fg_color=fg, 
            border_color=text_fg, 
            border_width=1, 
            text_color=text_fg
        )
        self.username_entry.pack(anchor="w", padx=(25, 0))

        ctk.CTkLabel(
            master=frame, 
            text="  Password:", 
            text_color=text_fg, 
            anchor="w", 
            justify="left", 
            font=("Helvetica", 14), 
            image=self.password_icon, 
            compound="left"
        ).pack(anchor="w", pady=(21, 0), padx=(25, 0))

        self.password_entry = ctk.CTkEntry(
            master=frame, 
            width=225, 
            fg_color=fg, 
            border_color=text_fg, 
            border_width=1, 
            text_color=text_fg,
            show="*"
        )
        self.password_entry.pack(anchor="w", padx=(25, 0))

        ctk.CTkButton(
            master=frame, 
            text="Sign In", 
            fg_color=btn_active, 
            hover_color=btn_hvr, 
            font=("Helvetica", 12), 
            text_color=text_fg_2, 
            command=self.verified,
            width=225
        ).pack(anchor="w", pady=(40, 0), padx=(25, 0))

        ctk.CTkButton(
            master=frame, 
            text="< Sign Up", 
            fg_color=bg, 
            hover_color=fg, 
            font=("Helvetica", 12), 
            text_color=text_fg, 
            command=self.signup,
            width=225, 
        ).pack(anchor="w", pady=(20, 0), padx=(25, 0))

    def signup(self):

        for widget in self.login_frame.winfo_children():
            widget.destroy()

        ctk.CTkLabel(master=self.login_frame, text="", image=self.side_img).pack(expand=True, side="right")

        frame = ctk.CTkFrame(master=self.login_frame, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="left")

        ctk.CTkLabel(
            master=frame, 
            text="Welcome!", 
            text_color=text_fg, 
            anchor="w", 
            justify="left", 
            font=("Helvetica", 24)
        ).pack(anchor="w", pady=(50, 5), padx=(25, 0))

        ctk.CTkLabel(
            master=frame, 
            text="Create a new account", 
            text_color="#7E7E7E",
            anchor="w",
            justify="left",
            font=("Helvetica", 12)
        ).pack(anchor="w", padx=(25, 0))

        ctk.CTkLabel(
            master=frame, 
            text="  Username:", 
            text_color=text_fg, 
            anchor="w", 
            justify="left", 
            font=("Helvetica", 14), 
            image=self.name_icon, 
            compound="left"
        ).pack(anchor="w", pady=(38, 0), padx=(25, 0))

        self.username_entry = ctk.CTkEntry(
            master=frame, 
            width=225, 
            fg_color=fg, 
            border_color=text_fg, 
            border_width=1, 
            text_color=text_fg
        )
        self.username_entry.pack(anchor="w", padx=(25, 0))

        ctk.CTkLabel(
            master=frame, 
            text="  Password:", 
            text_color=text_fg, 
            anchor="w", 
            justify="left", 
            font=("Helvetica", 14), 
            image=self.password_icon, 
            compound="left"
        ).pack(anchor="w", pady=(21, 0), padx=(25, 0))

        self.password_entry = ctk.CTkEntry(
            master=frame, 
            width=225, 
            fg_color=fg, 
            border_color=text_fg, 
            border_width=1, 
            text_color=text_fg,
            show="*"
        )
        self.password_entry.pack(anchor="w", padx=(25, 0))

        ctk.CTkButton(
            master=frame, 
            text="Sign Up", 
            fg_color=btn_active, 
            hover_color=btn_hvr, 
            font=("Helvetica", 12), 
            text_color=text_fg_2,
            command=self.create_account,
            width=225
        ).pack(anchor="w", pady=(40, 0), padx=(25, 0))

        ctk.CTkButton(
            master=frame, 
            text="Login >", 
            fg_color=bg, 
            hover_color=fg, 
            font=("Helvetica", 12), 
            text_color=text_fg, 
            command=self.login,
            width=225, 
        ).pack(anchor="w", pady=(20, 0), padx=(25, 0))

    def verified(self) -> bool:
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        if self.username == "" or self.password == "":
            messagebox.show_error("Login Failed", "All fields are required!")
            return False
        
        if accounts.verify_account(self.username, self.password):
            self.save_current_user()
            self.destroy()
            return True
    
        else:
            messagebox.show_error("Login Failed", "Invalid credentials!")
            return False

    def create_account(self) -> None:
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        if self.username == "" or self.password == "":
            messagebox.show_error("Signup Failed", "All fields are required!")
            return

        if accounts.verify_account(self.username, self.password):
            messagebox.show_error("Signup Failed", "Account already exists!")
            return

        try:
            accounts.add_account(self.username, self.password)
            messagebox.show_info("Signup Successful", "Account created successfully!")
        except Exception as e:
            messagebox.show_error("Signup Failed", f"Failed to create account: {e}")

    def save_current_user(self):
        with open(current_role_path, "w") as file:
                file.write(self.username + " " + self.password)
                