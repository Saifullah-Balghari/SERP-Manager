import customtkinter as ctk
from  PIL import Image, ImageTk
from tkinter import messagebox

from ..settings import *
from ..helpers import database as db

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"   
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"


class AddResult2DB(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("TopLevel - Add Results")
        self.geometry("1280x720")
        self.configure(fg_color=bg)
        self.resizable(False, False)

        self.widget()
    
    def widget(self):
        add_icon = ImageTk.PhotoImage(Image.open(add_exams_icon_path).resize((60, 60)), Image.LANCZOS) 

        title_label = ctk.CTkLabel(
            self,
            image=add_icon,
            compound="top",
            text="Add Results",
            font=("helvetica", 22, "bold"),
            text_color=text_fg
        )
        title_label.pack(fill="x", side="top", pady=(10, 0))

        sub_title_label = ctk.CTkLabel(
            self,
            text="Enter the details below, submit and wait for the confirmation message",
            font=("Helvetica", 12),
            text_color="grey"
        )
        sub_title_label.pack(side="top", fill="x",pady=(0, 5))

        main_frame = ctk.CTkFrame(master=self, fg_color=bg, border_width=2, border_color=btn_active)
        main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        result_form_frame = ctk.CTkFrame(main_frame, fg_color=bg)
        result_form_frame.pack(padx=30, pady=10, ipadx=20)