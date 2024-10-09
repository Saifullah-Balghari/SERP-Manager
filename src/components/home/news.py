import customtkinter as ctk

from ... settings import *
from .. import messagebox 

import os
import platform

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"   
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"


class GetNews():
    def __init__(self, news_n_updates, image):

        self.read_news_file()
    
        title_label = ctk.CTkLabel(
            news_n_updates,
            fg_color=bg,
            bg_color=bg,
            image=image,
            compound="top",
            text="News and Updates",
            text_color=text_fg,
            font=("Helvetica", -18, "bold")
        )
        title_label.pack(fill="x", pady=0, padx=0)

        # News frame
        news_frame = ctk.CTkFrame(news_n_updates, fg_color=bg)
        news_frame.pack(fill="x", padx=10, pady=10)

        for _, news_item in enumerate(self.news_list):
            news_button = ctk.CTkButton(
                news_frame,
                text=news_item,
                fg_color=fg,
                hover_color=btn_hvr,
                border_width=1,
                border_color=btn_active,
                text_color=text_fg,
                anchor="w",
                compound="left",
                image=icons["arrow_icon"],
                font=("Helvetica", -14),
                command=lambda n=news_item: self.open_pdf_for_news(n)
            )
            news_button.pack(fill="x", expand=True, padx=5, pady=5, ipadx=2, ipady=5)

    def read_news_file(self):
        try:
            with open(news_txt_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            self.news_list = [line.strip() for line in lines if line.strip()]
            return self.news_list

        except FileNotFoundError:
            messagebox.show_error("Error", f"News file not found at '{news_txt_path}'.")
            return []

    def open_pdf_for_news(self, news_item):

        pdf_files = [f for f in os.listdir(news_pdfs_path) if f.startswith(news_item) and f.endswith(".pdf")]

        if pdf_files:
            pdf_path = os.path.join(news_pdfs_path, pdf_files[0])
            self.open_pdf(pdf_path)
        else:
            messagebox.show_error("Error Opening", f"No PDF found for '{news_item}'")

    def open_pdf(self, pdf_path):
        try:
            if platform.system() == "Linux":
                os.system(f"xdg-open \"{pdf_path}\"")
            elif platform.system() == "Darwin":
                os.system(f"open \"{pdf_path}\"")
            elif platform.system() == "Windows":
                os.system(f"start \"\" \"{pdf_path}\"")
            else:
                messagebox.show_error("Error", "Unsupported OS")
        except Exception as e:
            messagebox.show_error("OS Error", f"Error opening PDF: {e}")
