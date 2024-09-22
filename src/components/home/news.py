import customtkinter as ctk

from ... settings import *

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"   
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

class GetNews():
    def __init__(self, news_n_updates, image):

        with open(news_txt_path, "rb") as f:
            lines = f.readlines()

        self.news_1 = lines[0].strip() if len(lines) > 0 else ""
        self.news_2 = lines[1].strip() if len(lines) > 1 else ""
        self.news_3 = lines[2].strip() if len(lines) > 2 else ""
        self.news_4 = lines[3].strip() if len(lines) > 3 else ""
    
        self.widgets(news_n_updates, image)

    def widgets(self, news_n_updates, image):

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

        # news 1
        news_1_frame = ctk.CTkFrame(news_frame, fg_color=fg, border_width=1, border_color=btn_active)
        news_1_frame.pack(fill="x", padx=5, pady=5)

        news_arrow = ctk.CTkLabel(
            news_1_frame,
            image=icons["arrow_icon"],
            text=""
        )
        news_arrow.pack(side="left", padx=5, pady=5)

        news_1_text = ctk.CTkLabel(
            news_1_frame,
            text=self.news_1,
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        news_1_text.pack(side="left", padx=5, pady=5)

        # news 2
        news_2_frame = ctk.CTkFrame(news_frame, fg_color=fg, border_width=1, border_color=btn_active)
        news_2_frame.pack(fill="x", padx=5, pady=5)

        news_arrow = ctk.CTkLabel(
            news_2_frame,
            image=icons["arrow_icon"],
            text=""
        )
        news_arrow.pack(side="left", padx=5, pady=5)

        news_2_text = ctk.CTkLabel(
            news_2_frame,
            text=self.news_2,
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        news_2_text.pack(side="left", padx=5, pady=5)

        # news 3
        news_3_frame = ctk.CTkFrame(news_frame, fg_color=fg, border_width=1, border_color=btn_active)
        news_3_frame.pack(fill="x", padx=5, pady=5)

        news_arrow = ctk.CTkLabel(
            news_3_frame,
            image=icons["arrow_icon"],
            text=""
        )
        news_arrow.pack(side="left", padx=5, pady=5)

        news_3_text = ctk.CTkLabel(
            news_3_frame,
            text=self.news_3,
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        news_3_text.pack(side="left", padx=5, pady=5)

        # news 4
        news_4_frame = ctk.CTkFrame(news_frame, fg_color=fg, border_width=1, border_color=btn_active)
        news_4_frame.pack(fill="x", padx=5, pady=5)

        news_arrow = ctk.CTkLabel(
            news_4_frame,
            image=icons["arrow_icon"],
            text=""
        )
        news_arrow.pack(side="left", padx=5, pady=5)

        news_4_text = ctk.CTkLabel(
            news_4_frame,
            text=self.news_4,
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        news_4_text.pack(side="left", padx=5, pady=5)
