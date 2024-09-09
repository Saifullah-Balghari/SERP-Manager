import customtkinter as ctk

from .settings import *

bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

class ManageNews(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("")

        self.title = ctk.CTkLabel(
            self,
            text="Edit the News",
            font=("Helvetica", 22, "bold"),
            fg_color=bg,
            text_color=text_fg
        )
        self.title.pack(fill="x", side="top", ipady=10)

        # Main frame
        self.main_frame = ctk.CTkFrame(self, fg_color=bg, corner_radius=0)
        self.main_frame.pack(fill="x", expand=True)

        # Load existing news from file
        self.load_existing_news()

        # News 1
        self.news_1_label = ctk.CTkLabel(
            self.main_frame,
            text="News 1:",
            text_color=text_fg,
            bg_color=bg,
            font=("Helvetica", 14)
        )
        self.news_1_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.news_1_entry = ctk.CTkEntry(
            self.main_frame,
            text_color=text_fg,
            bg_color=bg,
            width=600,
            font=("Helvetica", 14)
        )
        self.news_1_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.news_1_entry.insert(0, self.news_1)  # Insert existing news

        # News 2
        self.news_2_label = ctk.CTkLabel(
            self.main_frame,
            text="News 2:",
            text_color=text_fg,
            bg_color=bg,
            font=("Helvetica", 14)
        )
        self.news_2_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.news_2_entry = ctk.CTkEntry(
            self.main_frame,
            text_color=text_fg,
            bg_color=bg,
            font=("Helvetica", 14)
        )
        self.news_2_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.news_2_entry.insert(0, self.news_2)  # Insert existing news

        # News 3
        self.news_3_label = ctk.CTkLabel(
            self.main_frame,
            text="News 3:",
            text_color=text_fg,
            bg_color=bg,
            font=("Helvetica", 14),
        )
        self.news_3_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.news_3_entry = ctk.CTkEntry(
            self.main_frame,
            text_color=text_fg,
            bg_color=bg,
            font=("Helvetica", 14)
        )
        self.news_3_entry.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.news_3_entry.insert(0, self.news_3)  # Insert existing news

        # News 4
        self.news_4_label = ctk.CTkLabel(
            self.main_frame,
            text="News 4:",
            text_color=text_fg,
            bg_color=bg,
            font=("Helvetica", 14)
        )
        self.news_4_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.news_4_entry = ctk.CTkEntry(
            self.main_frame,
            text_color=text_fg,
            bg_color=bg,
            width=500,
            font=("Helvetica", 14)
        )
        self.news_4_entry.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        self.news_4_entry.insert(0, self.news_4)  # Insert existing news

        # Save and Cancel buttons
        self.save_button = ctk.CTkButton(
            self.main_frame,
            text="Save",
            text_color=text_fg_2,
            fg_color=btn_active,
            hover_color=btn_hvr,
            bg_color=bg,
            command=self.save_news
        )
        self.save_button.grid(row=4, column=0, padx=10, pady=10, ipadx=10,sticky="e")

        self.cancel_button = ctk.CTkButton(
            self.main_frame,
            text="Cancel",
            text_color=text_fg_2,
            fg_color=btn_active,
            bg_color=bg,
            hover_color=btn_hvr,
            command=self.destroy
        )
        self.cancel_button.grid(row=4, column=1, padx=10, pady=10, ipadx=10,sticky="w")

    def load_existing_news(self):
        # Initialize default news values
        self.news_1 = ""
        self.news_2 = ""
        self.news_3 = ""
        self.news_4 = ""
        
        # Read the existing news from the file
        try:
            with open(news_txt_path, "r") as f:
                news_lines = f.readlines()
                # Ensure there are exactly 4 lines
                if len(news_lines) >= 4:
                    self.news_1 = news_lines[0].strip()
                    self.news_2 = news_lines[1].strip()
                    self.news_3 = news_lines[2].strip()
                    self.news_4 = news_lines[3].strip()
        except FileNotFoundError:
            print("News file not found, starting with empty fields.")

    def save_news(self):
        # Update the news entries based on user input
        self.news_1 = self.news_1_entry.get() or self.news_1
        self.news_2 = self.news_2_entry.get() or self.news_2
        self.news_3 = self.news_3_entry.get() or self.news_3
        self.news_4 = self.news_4_entry.get() or self.news_4

        # Write the news to the file
        with open(news_txt_path, "w") as f:
            f.write(f"{self.news_1}\n{self.news_2}\n{self.news_3}\n{self.news_4}")
            print("News updated successfully!")

        # Close the window
        self.destroy()
