from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk

from .settings import *
from . import accounts

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

        self.login_frame = ctk.CTkFrame(self, fg_color=bg, corner_radius=0)
        self.login_frame.grid(sticky="nsew")

        self.acc_icon = Image.open(acc_icon_path).resize((300, 300), Image.LANCZOS)
        self.acc_icon_photo = ImageTk.PhotoImage(self.acc_icon)

        self.acc_icon_label = ctk.CTkLabel(
            self.login_frame,
            image=self.acc_icon_photo,
            text=""
        )
        self.acc_icon_label.grid(pady=20, padx=10, row=0, column=0, rowspan=8, sticky="nsew")

        self.login_label = ctk.CTkLabel(
            self.login_frame,
            text="Login Menu",
            text_color=text_fg,
            anchor="center",
            font=("Helvetica", 26, "bold")
        )
        self.login_label.grid(pady=10, padx=10, row=0, column=1, columnspan=2, sticky="nsew")

        self.username_label = ctk.CTkLabel(
            self.login_frame,
            text="Username:",
            text_color=text_fg,
            anchor="w",
            font=("Helvetica", 16)
        )
        self.username_label.grid(pady=(5, 0), padx=20, row=1, column=1, columnspan=2, sticky="ew")
        self.username_entry = ctk.CTkEntry(self.login_frame)
        self.username_entry.grid(pady=(0, 5), padx=20, row=2, column=1, columnspan=2, sticky="ew")

        self.password_label = ctk.CTkLabel(
            self.login_frame,
            text_color=text_fg,
            text="Password:",
            anchor="w",
            font=("Helvetica", 16)
        )
        self.password_label.grid(pady=(5, 0), padx=20, row=3, column=1, columnspan=2, sticky="ew")
        self.password_entry = ctk.CTkEntry(self.login_frame, show="*")
        self.password_entry.grid(pady=(0, 5), padx=20, row=4, column=1, columnspan=2, sticky="ew")

        self.role_label = ctk.CTkLabel(
            self.login_frame,
            text="Role:",
            text_color=text_fg,
            anchor="w",
            font=("Helvetica", 16)
        )
        self.role_label.grid(pady=(5, 0), padx=20, row=5, column=1, sticky="nsew")

        self.role_combobox = ctk.CTkOptionMenu(
            self.login_frame, 
            values=["Student", "Admin"], 
            fg_color=btn_active_2, 
            text_color=text_fg
        )
        self.role_combobox.grid(pady=(0, 5), padx=20, row=6, column=1, columnspan=2, sticky="ew")
        self.role_combobox.set("Student")

        self.signup_button = ctk.CTkButton(
            self.login_frame,
            text="Sign Up",
            text_color=text_fg,
            font=("Helvetica", 18, "bold"),
            command=self.signup,
            hover_color=bg,
            fg_color=btn_active_2
        )
        self.signup_button.grid(pady=20, padx=(20, 5), row=7, column=1)

        if self.role_combobox.get() == "Admin":
            self.signup_button.configure(state="disabled")

        self.login_button = ctk.CTkButton(
            self.login_frame,
            text="Sign In",
            text_color=text_fg_2,
            font=("Helvetica", 18, "bold"),
            command=self.verified,
            hover_color=btn_hvr,
            fg_color=btn_active
        )
        self.login_button.grid(pady=20, padx=(5, 20), row=7, column=2)

    def verified(self) -> bool:
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.role = self.role_combobox.get()

        if self.username == "" or self.password == "" or self.role == "":
            messagebox.showerror("Login Failed", "All fields are required!")
            return False
        
        if accounts.verify_account(self.username, self.password, self.role):
            self.save_current_user()
            self.destroy()
            return True
        
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")
            return False

    def signup(self) -> None:
        self.username: str = self.username_entry.get()
        self.password: str = self.password_entry.get()
        self.role: str = self.role_combobox.get()

        if self.username == "" or self.password == "" or self.role == "":
            messagebox.showerror("Signup Failed", "All fields are required!")
            return

        if accounts.verify_account(self.username, self.password, self.role):
            messagebox.showerror("Signup Failed", "Account already exists!")
            return

        try:
            accounts.add_account(self.username, self.password, self.role)
            messagebox.showinfo("Signup Successful", "Account created successfully!")
        except Exception as e:
            messagebox.showerror("Signup Failed", f"Failed to create account: {e}")

    def save_current_user(self):
        with open(current_role_path, "w") as file:
                file.write(self.username + " " + self.role)