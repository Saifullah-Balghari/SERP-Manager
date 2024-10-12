import customtkinter as ctk

from ...settings import *

import webbrowser

bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

class ContactUs(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Toplevel - Contact Us")
        self.geometry("600x300")
        self.resizable(0, 0) 
        self.configure(fg_color=fg)
        self.attributes("-topmost", True)
        self.update()
        self.grab_set()

        self.main_frame = ctk.CTkFrame(self, fg_color=bg)
        self.main_frame.pack(fill="both", expand="true", padx=0, pady=0)

        contact_us_frame = ctk.CTkFrame(self.main_frame, fg_color=bg)
        contact_us_frame.pack(fill="x", expand="true", padx=20, pady=20)

        title = ctk.CTkLabel(
            contact_us_frame,
            text="Contact Us Through here...",
            text_color=text_fg,
            font=("Helvetica", -18, "bold"),
        )
        title.pack(fill="x", pady=(10, 0))

        btn_frame = ctk.CTkFrame(contact_us_frame, fg_color=bg)
        btn_frame.pack(pady=10)

        # GitHub
        ctk.CTkButton(
                btn_frame,
                text="GitHub",
                fg_color=bg,
                text_color=text_fg,
                hover_color=fg,
                width=100,
                height=100,
                command=lambda: webbrowser.open("http://github.com/Saifullah-Balghari"),
                image=icons["github"],
                compound="top",
                font=("helvetica", 16)
        ).pack(side="left", padx=10, pady=10, ipadx=5, ipady=5)
        
        # YouTube
        ctk.CTkButton(
                btn_frame,
                text="YouTube",
                fg_color=bg,
                text_color=text_fg,
                hover_color=fg,
                width=100,
                height=100,                
                command=lambda: webbrowser.open("https://www.youtube.com/@saifullahbalghari"),
                image=icons["youtube"],
                compound="top",
                font=("helvetica", 16)
        ).pack(side="left", padx=10, pady=10, ipadx=5, ipady=5)

        # LinkedIn
        ctk.CTkButton(
                btn_frame,
                text="LinkedIn",
                fg_color=bg,
                text_color=text_fg,
                hover_color=fg,
                command=lambda: webbrowser.open("https://www.linkedin.com/in/saifullah-balghari/"),
                width=100,
                height=100,
                image=icons["linkedin"],
                compound="top",
                font=("helvetica", 16)
        ).pack(side="left", padx=10, pady=10, ipadx=5, ipady=5)

        # Instagram
        ctk.CTkButton(
                btn_frame,
                text="Instagram",
                fg_color=bg,
                text_color=text_fg,
                hover_color=fg,
                command=lambda: webbrowser.open("http://github.com/Saifullah-Balghari"),               
                width=100,
                height=100,
                image=icons["instagram"],
                compound="top",
                font=("helvetica", 16)
        ).pack(side="left", padx=10, pady=10, ipadx=5, ipady=5)


