# Disclaimer:
# Icons are not designed by me, sourced from www.flaticon.com

# This is a simple GUI Application that can be used as an Examinations, Results and Paper Manager.
# As of now this project is a personal side project and is not intended for commercial use or distribution.

# External imports
import customtkinter as ctk
from tkinter import messagebox, filedialog      # tk
from pdf2image import convert_from_path
from PIL import Image, ImageTk                  # pillow

# Inbuilt imports
import platform
import warnings
import logging
import json
import shutil
import os

# Set the default path as "..\..\..\..\..\..\SERP-Manager"
base_path = r'/home/sbalghari/Documents/GitHub/SERP-Manager'
path = "/home/sbalghari/Documents/GitHub/SERP-Manager/current_role.txt"

# Default settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Icons
ADD_ICON_PATH = os.path.join(base_path, "Icons", "add.png")
EXAM_ICON_PATH = os.path.join(base_path, "Icons", "exam.png")
HOME_ICON_PATH = os.path.join(base_path, "Icons", "home.png")
PAPERS_ICON_PATH = os.path.join(base_path, "Icons", "papers.png")
REFRESH_ICON_PATH = os.path.join(base_path, "Icons", "refresh.png")
DELETE_ICON_PATH = os.path.join(base_path, "Icons", "remove.png")
RESULT_ICON_PATH = os.path.join(base_path, "Icons", "results.png")
EXAM_SHORTCUT_ICON_PATH = os.path.join(base_path, "Icons", "exam_shortcut.png")
PAPER_SHORTCUT_ICON_PATH = os.path.join(base_path, "Icons", "paper_shortcut.png")
RESULT_SHORTCUT_ICON_PATH = os.path.join(base_path, "Icons", "result_shortcut.png")
CONTACT_US_ICON_PATH = os.path.join(base_path, "Icons", "contact_us.png")
ADD_EXAMS_ICON_PATH = os.path.join(base_path, "Icons", "add_exam.png")
SUPPORT_ICON_PATH = os.path.join(base_path, "Icons", "support.png")
NEWS_ICON_PATH = os.path.join(base_path, "Icons", "news.png")
STUDENTS_ICON_PATH = os.path.join(base_path, "Icons", "student.png")
TEACHERS_ICON_PATH = os.path.join(base_path, "Icons", "staff.png")
RIGHT_ARROW_ICON_PATH = os.path.join(base_path, "Icons", "right_arrow.png")
EDIT_ICON_PATH = os.path.join(base_path, "Icons", "edit.png")
LOGOUT_ICON_PATH = os.path.join(base_path, "Icons", "logout.png")

# Icons of Subjects
MATHS_ICON_PATH = os.path.join(base_path, "Icons", "math.png")
BIOLOGY_ICON_PATH = os.path.join(base_path, "Icons", "bio.png")
ENGLISH_ICON_PATH = os.path.join(base_path, "Icons", "eng.png")
URDU_ICON_PATH = os.path.join(base_path, "Icons", "urdu.png")
PHYSICS_ICON_PATH = os.path.join(base_path, "Icons", "phy.png")
CHEMISTRY_ICON_PATH = os.path.join(base_path, "Icons", "chemistry.png")
COMPUTER_ICON_PATH = os.path.join(base_path, "Icons", "cs.png")
ISLAMIYAT_ICON_PATH = os.path.join(base_path, "Icons", "islamiyat.png")
PK_STD_ICON_PATH = os.path.join(base_path, "Icons", "ps.png")

# Paths
DEFAULT_PDFs_PATH = os.path.join(base_path, "Papers")
CACHE_FOLDER_PATH = os.path.join(base_path, "Cache")

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

# Window size
WIDTH = 1366
HEIGHT = 768

class SERPManagerGUI():
    def __init__(self):

        try:
            if not os.path.exists(CACHE_FOLDER_PATH):
                os.makedirs(CACHE_FOLDER_PATH)

            # Variables declarations
            self.selected_button = None
            self.role = "student"

            # Load the current role from the file
            with open(path, 'r') as f:
                self.role = f.read().strip().lower()
                if self.role not in ["student", "admin"]:
                    raise ValueError("Invalid role")

            # Converts and resize the PNG to ctkimage for buttons
            self.refresh_pdfs_button_icon = ctk.CTkImage(Image.open(REFRESH_ICON_PATH).resize((18, 18), Image.LANCZOS))
            self.add_paper_button_icon = ctk.CTkImage(Image.open(ADD_ICON_PATH).resize((18, 18), Image.LANCZOS))
            self.delete_paper_button_icon = ctk.CTkImage(Image.open(DELETE_ICON_PATH).resize((18, 18), Image.LANCZOS))
            self.HOME_ICON = ctk.CTkImage(Image.open(HOME_ICON_PATH).resize((26, 26), Image.LANCZOS))
            self.PAPERS_ICON = ctk.CTkImage(Image.open(PAPERS_ICON_PATH).resize((26, 26), Image.LANCZOS))
            self.EXAM_ICON = ctk.CTkImage(Image.open(EXAM_ICON_PATH).resize((26, 26), Image.LANCZOS))
            self.RESULT_ICON = ctk.CTkImage(Image.open(RESULT_ICON_PATH).resize((26, 26), Image.LANCZOS))
            self.contact_us_button_icon = ctk.CTkImage(Image.open(CONTACT_US_ICON_PATH).resize((18, 18), Image.LANCZOS))
            self.add_exams_button_icon = ctk.CTkImage(Image.open(ADD_EXAMS_ICON_PATH).resize((18, 18), Image.LANCZOS))
            self.edit_button_icon = ctk.CTkImage(Image.open(EDIT_ICON_PATH).resize((18, 18), Image.LANCZOS))
            self.logout_button_icon = ctk.CTkImage(Image.open(LOGOUT_ICON_PATH).resize((18, 18), Image.LANCZOS))

            try:
                # Create the main application window
                self.root = ctk.CTk()

                # Window configurations
                self.root.title("SERP-Manager (Developed By Saifullah Balghari)")
                self.root.geometry(f"{WIDTH}x{HEIGHT}")
                self.root.resizable(False, False)
                self.root.iconbitmap(None, None)
                self.root.grid_rowconfigure(0, weight=1)
                self.root.grid_rowconfigure(1, weight=15)
                self.root.grid_columnconfigure(0, weight=1)

                # Create the header frame
                self.create_header_frame()

                # Create the main frame
                self.create_main_frame()

                # Run the main loop
                self.root.mainloop()

            except Exception as e:
                messagebox.showerror("Error", f"Failed to initialize the application: {e}")
                print(e)
        except Exception as e:
            messagebox.showerror( "Error", f"An exception occurred in the Constructor: {e}")
            print(e)


    def create_header_frame(self):

        # Create the header frame
        self.header_frame = ctk.CTkFrame(self.root, fg_color=bg, corner_radius=0)
        self.header_frame.grid(padx=0, pady=(0, 10), row=0, column=0, sticky="nsew")

        # Header frame configuration
        self.header_frame.grid_propagate(False)
        self.header_frame.configure(height=35)
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=1)
        self.header_frame.grid_columnconfigure(2, weight=1)

        # Create the button frame
        button_frame = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        button_frame.grid(padx=0, pady=0, row=0, column=1, sticky="nsew")
        button_frame.grid_propagate(False)

        # Button frame configuration
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)
        button_frame.grid_columnconfigure(3, weight=1)

        # Home button
        self.home_button = ctk.CTkButton(
            button_frame,
            text="Home",
            text_color=text_fg,
            font=("Helvetica", 22, "bold"),
            hover_color=btn_hvr,
            width=15,
            height=40,
            image=self.HOME_ICON,
            compound="left",
            anchor="center",
            command=self.show_home
        )
        self.home_button.grid(padx=(10,5), pady=10, row=0, column=0, sticky="nsew")

        # Exams button
        self.exams_button = ctk.CTkButton(
            button_frame,
            text="Exams",
            font=("Helvetica", 22, "bold"),
            hover_color=btn_hvr,
            width=15,
            height=40,
            image=self.EXAM_ICON,
            compound="left",
            text_color=text_fg,
            anchor="center",
            command=self.show_examinations
        )
        self.exams_button.grid(padx=(5,5), pady=10, row=0, column=1, sticky="nsew")

        # Results button
        self.results_button = ctk.CTkButton(
            button_frame,
            text="Results",
            font=("Helvetica", 22, "bold"),
            hover_color=btn_hvr,
            width=15,
            height=40,
            image=self.RESULT_ICON,
            compound="left",
            anchor="center",
            text_color=text_fg,
            command=self.show_results
        )
        self.results_button.grid(padx=(5,5), pady=10, row=0, column=2, sticky="nsew")

        # Papers button
        self.papers_button = ctk.CTkButton(
            button_frame,
            text="Papers",
            font=("Helvetica", 22, "bold"),
            hover_color=btn_hvr, width=15,
            height=40,
            image=self.PAPERS_ICON,
            compound="left",
            anchor="center",
            text_color=text_fg,
            command=self.show_papers
        )
        self.papers_button.grid(padx=(5,10), pady=10, row=0, column=3, sticky="nsew")

    def create_main_frame(self):

        # Create the main frame
        self.main_frame = ctk.CTkFrame(self.root, fg_color=bg, corner_radius=0)
        self.main_frame.grid(padx=0, pady=0, row=1, column=0, sticky="nsew")

        # Main frame configuration
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_propagate(False)

        # Set the home section as the main frame
        self.show_home()

    def set_button_state(self, selected_button):

        # Reset the button state
        for button in [self.home_button, self.exams_button, self.results_button, self.papers_button]:
            button.configure(fg_color="transparent", text_color=text_fg)

        # Set the selected button state
        selected_button.configure(text_color=text_fg_2, fg_color=btn_active)

    def show_home(self):
        """
        Code Hierarchy:

        -> main_frame
            > wellcome_message_frame
            > main_scrollable_frame
                > about_n_shortcuts_frame
                    > shortcut_1_frame
                    > shortcut_2_frame
                    > shortcut_3_frame
                > news_n_updates
                    > title_frame
                    > news_frame
                        > news_1_frame
                        > news_2_frame
                        > news_3_frame
                        > news_4_frame
                > about_roles_and_help
                    > role_1_frame
                    > role_2_frame
                    > help_frame
            > buttons_frame
                > contact_us_button
                > edit_news_button
                > refresh_button
                > logout_button
                > close_button
        """

        # Clear the main frame and set the button state
        self.clear_main_frame()
        self.set_button_state(self.home_button)

        # Wellcome message frame
        wellcome_message_frame = ctk.CTkFrame(self.main_frame, height=80, fg_color=bg)
        wellcome_message_frame.pack(side="top", fill="x", padx=10, pady=(20, 0))

        # Title Label
        logo_label = ctk.CTkLabel(
            wellcome_message_frame,
            text="Welcome To SERP-Manager",
            text_color=text_fg,
            font=("Helvetica", 36, "bold")
        )
        logo_label.pack(side="top", fill="x")

        # Introduction Label
        intro_label = ctk.CTkLabel(
            wellcome_message_frame,
            text="Manage examinations, results, and much more...",
            text_color=text_fg,
            font=("Helvetica", 16)
        )
        intro_label.pack(side="top", fill="x")

        # Main Scrollable Frame
        main_scrollable_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color=bg)
        main_scrollable_frame.pack(fill="both", expand="true", padx=10, pady=0, ipadx=0, ipady=0)

        # Shortcuts Frame
        about_n_shortcuts_frame = ctk.CTkFrame(main_scrollable_frame, fg_color=bg)
        about_n_shortcuts_frame.pack(side="top", fill="x", expand="true", padx=5, pady=0)

        # Shortcut 1
        shortcut_1_frame = ctk.CTkFrame(about_n_shortcuts_frame, fg_color=fg)
        shortcut_1_frame.grid(row=0, column=0, padx=30, pady=10, sticky="nsew")

        img = Image.open(PAPER_SHORTCUT_ICON_PATH).resize((100, 100), Image.LANCZOS)
        shortcut_1_icon = ImageTk.PhotoImage(img)

        shortcut_1_icon = ctk.CTkLabel(shortcut_1_frame, text="", image=shortcut_1_icon, height=120, width=120)
        shortcut_1_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        shortcut_1_text = ctk.CTkLabel(
            shortcut_1_frame,
            text="Papers",
            text_color=text_fg,
            font=("Helvetica", 16)
        )
        shortcut_1_text.grid(row=0, column=1, padx=10, pady=(10, 0))

        shortcut_1_sub_text = ctk.CTkLabel(
            shortcut_1_frame,
            text="Keep track of your past and\n model papers, read them, delete them\n and add more papers etc.",
            text_color=text_fg,
            font=("Helvetica", 12)
        )
        shortcut_1_sub_text.grid(row=1, column=1, padx=10, pady=0)

        go_to_papers_button = ctk.CTkButton(
            shortcut_1_frame,
            text="Go to papers ->",
            fg_color=btn_active,
            hover_color=btn_hvr,
            width=50,
            height=10,
            command=self.show_papers
        )
        go_to_papers_button.grid(row=2, column=1, padx=10, ipadx=1, ipady=1, pady=(0, 10))

        # Shortcut 2
        shortcut_2_frame = ctk.CTkFrame(about_n_shortcuts_frame, fg_color=fg)
        shortcut_2_frame.grid(row=0, column=1, padx=30, pady=10, sticky="nsew")

        img = Image.open(EXAM_SHORTCUT_ICON_PATH).resize((100, 100), Image.LANCZOS)
        shortcut_2_icon = ImageTk.PhotoImage(img)

        shortcut_2_icon = ctk.CTkLabel(
            shortcut_2_frame,
            text="",
            image=shortcut_2_icon,
            height=120,
            width=120
        )
        shortcut_2_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        shortcut_2_text = ctk.CTkLabel(
            shortcut_2_frame,
            text="Examinations",
            text_color=text_fg,
            font=("Helvetica", 16)
        )
        shortcut_2_text.grid(row=0, column=1, padx=10, pady=(10, 0))

        shortcut_2_sub_text = ctk.CTkLabel(
            shortcut_2_frame,
            text="Stay up to date with ongoing\n examination's datesheets. Teachers will be able\nto change, remove or add exams.",
            text_color=text_fg,
            font=("Helvetica", 12)
        )
        shortcut_2_sub_text.grid(row=1, column=1, padx=10, pady=0)

        go_to_exams_button = ctk.CTkButton(
            shortcut_2_frame,
            text="Go to Exams ->",
            fg_color=btn_active,
            hover_color=btn_hvr,
            width=50,
            height=10,
            command=self.show_examinations
            )
        go_to_exams_button.grid(row=2, column=1, padx=10, ipady=1, ipadx=1, pady=(0, 10))

        # Shortcut 3
        shortcut_3_frame = ctk.CTkFrame(about_n_shortcuts_frame, fg_color=fg)
        shortcut_3_frame.grid(row=0, column=2, padx=30, pady=10, sticky="nsew")

        img = Image.open(RESULT_SHORTCUT_ICON_PATH).resize((100, 100), Image.LANCZOS)
        shortcut_3_icon = ImageTk.PhotoImage(img)

        shortcut_3_icon = ctk.CTkLabel(shortcut_3_frame, text="", image=shortcut_3_icon, height=120, width=120)
        shortcut_3_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        shortcut_3_text = ctk.CTkLabel(
            shortcut_3_frame,
            text="Results",
            text_color=text_fg,
            font=("Helvetica", 16)
        )
        shortcut_3_text.grid(row=0, column=1, padx=10, pady=(10, 0))

        shortcut_3_sub_text = ctk.CTkLabel(
            shortcut_3_frame,
            text="See the results of recent\n examination. The teachers will be able\nto add and remove the results.",
            text_color=text_fg,
            font=("Helvetica", 12)
        )
        shortcut_3_sub_text.grid(row=1, column=1, padx=10, pady=0)

        go_to_results_button = ctk.CTkButton(
            shortcut_3_frame,
            text="Go to Results ->",
            fg_color=btn_active,
            hover_color=btn_hvr,
            width=50,
            height=10,
            command=self.show_results
            )
        go_to_results_button.grid(row=2, column=1, padx=10, ipady=1, ipadx=1, pady=(0, 10))

        # news and updates frame
        news_n_updates = ctk.CTkFrame(main_scrollable_frame, fg_color=bg)
        news_n_updates.pack(side="top", fill="both", padx=5, pady=0)

        img = Image.open(NEWS_ICON_PATH).resize((60, 60), Image.LANCZOS)
        news_icon = ImageTk.PhotoImage(img)

        title_frame = ctk.CTkFrame(news_n_updates, fg_color=bg, bg_color=bg)
        title_frame.pack(side="top", fill="x", padx=10, pady=0)

        news_icon = ctk.CTkLabel(
            title_frame,
            text="",
            image=news_icon,
            height=120,
            width=120
        )
        news_icon.grid(row=0, column=0, sticky="w", padx=(10, 0), pady=0)
        title_label = ctk.CTkLabel(
            title_frame,
            fg_color=bg,
            bg_color=bg,
            text="News and Updates",
            text_color=text_fg,
            font=("Helvetica", 26, "bold")
        )
        title_label.grid(row=0, column=1, sticky="w", padx=(0, 10), pady=0)

        # News frame
        news_frame = ctk.CTkFrame(news_n_updates, fg_color=bg, corner_radius=0)
        news_frame.pack(fill="x", padx=30, pady=(0, 10))

        with open(f"{base_path}/news.txt", "rb") as f:
            lines = f.readlines()

        self.news_1 = lines[0].strip() if len(lines) > 0 else ""
        self.news_2 = lines[1].strip() if len(lines) > 1 else ""
        self.news_3 = lines[2].strip() if len(lines) > 2 else ""
        self.news_4 = lines[3].strip() if len(lines) > 3 else ""

        img = Image.open(RIGHT_ARROW_ICON_PATH).resize((20, 20), Image.LANCZOS)
        arrow_icon = ImageTk.PhotoImage(img)

        # news 1
        news_1_frame = ctk.CTkFrame(news_frame, fg_color=fg)
        news_1_frame.pack(fill="x", padx=0, pady=(0, 2))

        news_arrow = ctk.CTkLabel(
            news_1_frame,
            image=arrow_icon,
            text=""
        )
        news_arrow.pack(side="left", padx=10, pady=0)

        news_1_text = ctk.CTkLabel(
            news_1_frame,
            text=self.news_1,
            text_color=text_fg,
            font=("Helvetica", 14)
        )
        news_1_text.pack(side="left", padx=10, pady=0, ipadx=5, ipady=5)

        # news 2
        news_2_frame = ctk.CTkFrame(news_frame, fg_color=fg)
        news_2_frame.pack(fill="x", padx=0, pady=2)

        news_arrow = ctk.CTkLabel(
            news_2_frame,
            image=arrow_icon,
            text=""
        )
        news_arrow.pack(side="left", padx=10, pady=0)

        news_2_text = ctk.CTkLabel(
            news_2_frame,
            text=self.news_2,
            text_color=text_fg,
            font=("Helvetica", 14)
        )
        news_2_text.pack(side="left", padx=10, pady=0, ipadx=5, ipady=5)

        # news 3
        news_3_frame = ctk.CTkFrame(news_frame, fg_color=fg)
        news_3_frame.pack(fill="x", padx=0, pady=2)

        news_arrow = ctk.CTkLabel(
            news_3_frame,
            image=arrow_icon,
            text=""
        )
        news_arrow.pack(side="left", padx=10, pady=0)

        news_3_text = ctk.CTkLabel(
            news_3_frame,
            text=self.news_3,
            text_color=text_fg,
            font=("Helvetica", 14)
        )
        news_3_text.pack(side="left", padx=10, pady=0, ipadx=5, ipady=5)

        # news 4
        news_4_frame = ctk.CTkFrame(news_frame, fg_color=fg)
        news_4_frame.pack(fill="x", padx=0, pady=2)

        news_arrow = ctk.CTkLabel(
            news_4_frame,
            image=arrow_icon,
            text=""
        )
        news_arrow.pack(side="left", padx=10, pady=0)

        news_4_text = ctk.CTkLabel(
            news_4_frame,
            text=self.news_4,
            text_color=text_fg,
            font=("Helvetica", 14)
        )
        news_4_text.pack(side="left", padx=10, pady=0, ipadx=5, ipady=5)

        # about us and Roles frame
        about_roles_and_us = ctk.CTkFrame(main_scrollable_frame, fg_color=bg)
        about_roles_and_us.pack(side="top", fill="both", padx=30, pady=(20, 10))

        # admin role
        role_1_frame = ctk.CTkFrame(about_roles_and_us, fg_color=fg)
        role_1_frame.grid(row=0, column=0, padx=7, pady=20, sticky="nsew")

        img = Image.open(TEACHERS_ICON_PATH).resize((100, 100), Image.LANCZOS)
        role_1_icon = ImageTk.PhotoImage(img)

        role_1_icon = ctk.CTkLabel(role_1_frame, text="", image=role_1_icon, height=120, width=120)
        role_1_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        role_1_text = ctk.CTkLabel(
            role_1_frame,
            text="Teachers",
            text_color=text_fg,
            font=("Helvetica", 18)
        )
        role_1_text.grid(row=0, column=1, padx=11, pady=(10, 0))

        role_1_sub_text = ctk.CTkLabel(
            role_1_frame,
            text="This role is for the staff of the school.\n They will have access to all features, they\n will be able to add, edit or remove\n exams, results and papers.",
            text_color=text_fg,
            font=("Helvetica", 13)
        )
        role_1_sub_text.grid(row=1, column=1, padx=11, pady=0)

        # student role
        role_2_frame = ctk.CTkFrame(about_roles_and_us, fg_color=fg)
        role_2_frame.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

        img = Image.open(STUDENTS_ICON_PATH).resize((100, 100), Image.LANCZOS)
        role_2_icon = ImageTk.PhotoImage(img)

        role_2_icon = ctk.CTkLabel(role_2_frame, text="", image=role_2_icon, height=120, width=120)
        role_2_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        role_2_text = ctk.CTkLabel(
            role_2_frame,
            text="Students",
            text_color=text_fg,
            font=("Helvetica", 18)
        )
        role_2_text.grid(row=0, column=1, padx=10, pady=(10, 0))

        role_2_sub_text = ctk.CTkLabel(
            role_2_frame,
            text="This is the role for students.\nThey will not be able to access any exclusive\n features but they will be able to see news,\n exam datesheets, results and papers.",
            text_color=text_fg,
            font=("Helvetica", 13)
        )
        role_2_sub_text.grid(row=1, column=1, padx=10, pady=0)

        # help & feedback
        help_frame = ctk.CTkFrame(about_roles_and_us, fg_color=fg)
        help_frame.grid(row=0, column=2, padx=10, pady=20, sticky="nsew")

        img = Image.open(SUPPORT_ICON_PATH).resize((100, 100), Image.LANCZOS)
        help_icon = ImageTk.PhotoImage(img)

        about_us_icon = ctk.CTkLabel(help_frame, text="", image=help_icon, height=120, width=120)
        about_us_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        help_text = ctk.CTkLabel(
            help_frame,
            text="Help & Feedback",
            text_color=text_fg,
            font=("Helvetica", 18)
        )
        help_text.grid(row=0, column=1, padx=10, pady=(10, 5))

        help_sub_text = ctk.CTkLabel(
            help_frame,
            text="Have you been in any kind of issue\n while using our program and want it to be\n fixed? Please let us know and we will try\n our best to fix it ASAP.",
            text_color=text_fg,
            font=("Helvetica", 13)
        )
        help_sub_text.grid(row=1, column=1, padx=10, ipadx=5, pady=5)

        # buttons frame
        buttons_frame = ctk.CTkFrame(self.main_frame, fg_color=bg)
        buttons_frame.pack(side="bottom", fill="x", padx=10, pady=(0, 5))

        # close button
        close_btn = ctk.CTkButton(
            buttons_frame,
            text="Close",
            text_color=text_fg,
            hover_color=btn_hvr,
            border_width=1,
            border_color=text_fg,
            fg_color=bg,
            command=self.root.destroy
        )
        close_btn.pack(side="right", padx=5, pady=5)

        # logout button
        logout_btn = ctk.CTkButton(
            buttons_frame,
            text="Logout",
            command=self.logout,
            text_color=text_fg_2,
            image=self.logout_button_icon,
            hover_color=btn_hvr,
            fg_color=btn_active,
        )
        logout_btn.pack(side="right", padx=5, pady=5)

        # Contact us button
        contact_us_button = ctk.CTkButton(
            buttons_frame,
            text="Contact Us",
            command=self.show_contact_us,
            text_color=text_fg_2,
            hover_color=btn_hvr,
            image=self.contact_us_button_icon,
            fg_color=btn_active,
        )
        contact_us_button.pack(side="left", padx=5, pady=5)

        if self.role == "admin":
            # Edit news button
            add_news_button = ctk.CTkButton(
                buttons_frame,
                text="Edit News",
                command=self.show_edit_news,
                text_color=text_fg_2,
                image=self.edit_button_icon,
                hover_color=btn_hvr,
                fg_color=btn_active,
            )
            add_news_button.pack(side="left", padx=5, pady=5)

            # Refresh button
            refresh_button = ctk.CTkButton(
                buttons_frame,
                text="Refresh",
                image=self.refresh_pdfs_button_icon,
                command=self.create_main_frame,
                text_color=text_fg_2,
                hover_color=btn_hvr,
                fg_color=btn_active,
            )
            refresh_button.pack(side="left", padx=5, pady=5)

    def show_examinations(self):
        """
        Code Hierarchy:

        -> scrollable_frame
            > current_exams
                > content_frame
                    > ssc_exams_frame
                        > ssc_contents_frame
                            > ssc_1_frame
                                > ssc_1_content_frame
                            > ssc_2_frame
                                > ssc_2_content_frame
                            > ssc_current_exams_config_btn_frame
                    > hssc_exams_frame
                        > hssc_contents_frame
                            > hssc_1_frame
                                > hssc_1_content_frame
                            > hssc_2_frame
                                > hssc_2_content_frame
                            > hssc_current_exams_config_btn_frame
            > about_exams_frame
                > exams_info_content_frame
                    > assessment_info_frame
                    > term_info_frame
                    > preboard_info_frame
                    > final_info_frame
        """
        # Clear the main frame and set the button state
        self.clear_main_frame()
        self.set_button_state(self.exams_button)

        # Subjects Icons
        img1 = Image.open(PHYSICS_ICON_PATH).resize((100, 100), Image.LANCZOS)
        phy_icon = ImageTk.PhotoImage(img1)
        img2 = Image.open(CHEMISTRY_ICON_PATH).resize((100, 100), Image.LANCZOS)
        chem_icon = ImageTk.PhotoImage(img2)
        img3 = Image.open(BIOLOGY_ICON_PATH).resize((100, 100), Image.LANCZOS)
        bio_icon = ImageTk.PhotoImage(img3)
        img4 = Image.open(COMPUTER_ICON_PATH).resize((100, 100), Image.LANCZOS)
        cs_icon = ImageTk.PhotoImage(img4)
        img5 = Image.open(ISLAMIYAT_ICON_PATH).resize((100, 100), Image.LANCZOS)
        isl_icon = ImageTk.PhotoImage(img5)
        img6 = Image.open(MATHS_ICON_PATH).resize((100, 100), Image.LANCZOS)
        math_icon = ImageTk.PhotoImage(img6)
        img7 = Image.open(URDU_ICON_PATH).resize((100, 100), Image.LANCZOS)
        urdu_icon = ImageTk.PhotoImage(img7)
        img8 = Image.open(PK_STD_ICON_PATH).resize((100, 100), Image.LANCZOS)
        ps_icon = ImageTk.PhotoImage(img8)
        img9 = Image.open(ENGLISH_ICON_PATH).resize((100, 100), Image.LANCZOS)
        eng_icon = ImageTk.PhotoImage(img9)

        # Create the scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color=bg
        )
        scrollable_frame.grid(row=0, column=0, padx=10, pady=(0, 0), sticky="nsew")

        # Ongoing Exams
        current_exams = ctk.CTkFrame(scrollable_frame, fg_color=bg)
        current_exams.pack(fill="x", padx=10, pady=(0, 0))

        # Title
        current_exams_label = ctk.CTkLabel(
            current_exams,
            text="Current Exams",
            text_color=text_fg,
            fg_color=bg,
            font=("Helvetica", 22, "bold")
        )
        current_exams_label.pack(fill="x", padx=10, pady=5)

        # Main content frame
        content_frame = ctk.CTkFrame(current_exams, fg_color=bg)
        content_frame.pack(fill="x", padx=0, pady=0)

        # SSC Exams
        ssc_exams_frame = ctk.CTkFrame(content_frame)
        ssc_exams_frame.pack(side="top", fill="x", padx=(0, 0), pady=0)

        ssc_label = ctk.CTkLabel(
            ssc_exams_frame,
            text="SSC Exams",
            text_color=text_fg,
            fg_color=bg,
            font=("Helvetica", 16, "bold")
        )
        ssc_label.pack(fill="x")

        # SSC content frame
        ssc_contents_frame = ctk.CTkFrame(ssc_exams_frame, fg_color=bg)
        ssc_contents_frame.pack(fill="x", padx=0, pady=0, expand="true")

        # SSC-I
        ssc_1_frame = ctk.CTkFrame(ssc_contents_frame, fg_color=bg)
        ssc_1_frame.pack(side="top", fill="x", padx=(0, 0), pady=0, ipady=0)

        ssc_1_label = ctk.CTkLabel(
            ssc_1_frame,
            text="SSC-I",
            text_color=text_fg,
        )
        ssc_1_label.pack(fill="x")

        # SSC-I contents
        self.ssc_1_content_frame = ctk.CTkScrollableFrame(ssc_1_frame, fg_color=bg, orientation="horizontal")
        self.ssc_1_content_frame.pack(fill="x", padx=0, pady=0, ipady=0)

        # SSC-II
        ssc_2_frame = ctk.CTkFrame(ssc_contents_frame, fg_color=bg)
        ssc_2_frame.pack(side="top", fill="x", padx=(0, 0), pady=0, ipady=0)

        ssc_2_label = ctk.CTkLabel(
            ssc_2_frame,
            text="SSC-II",
            text_color=text_fg,
        )
        ssc_2_label.pack(fill="x")

        # SSC-II contents
        self.ssc_2_content_frame = ctk.CTkScrollableFrame(ssc_2_frame, fg_color=bg, orientation="horizontal")
        self.ssc_2_content_frame.pack(fill="x", padx=0, pady=0, ipady=0)

        if self.role == "admin":
            # SSC frame buttons
            ssc_current_exams_config_btn_frame = ctk.CTkFrame(ssc_contents_frame, fg_color=bg)
            ssc_current_exams_config_btn_frame.pack(side="top", fill="x", padx=(0, 0), pady=5)

            # Add SSC-I Exam
            add_ssc_1_exam_btn = ctk.CTkButton(
                ssc_current_exams_config_btn_frame,
                image=self.add_exams_button_icon,
                text="Add SSC-I Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            add_ssc_1_exam_btn.grid(row=0, column=0,padx=5, pady=5, sticky="we")

            # Remove SSC-I Exam
            remove_ssc_1_exam_btn = ctk.CTkButton(
                ssc_current_exams_config_btn_frame,
                image=self.delete_paper_button_icon,
                text="Remove SSC-I Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            remove_ssc_1_exam_btn.grid(row=0, column=1, padx=5, pady=5, sticky="we")

            # Add SSC-II Exam
            add_ssc_2_exam_btn = ctk.CTkButton(
                ssc_current_exams_config_btn_frame,
                image=self.add_exams_button_icon,
                text="Add SSC-II Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            add_ssc_2_exam_btn.grid(row=0, column=2, padx=5, pady=5, sticky="we")

            # Remove SSC-II Exam
            remove_ssc_2_exam_btn = ctk.CTkButton(
                ssc_current_exams_config_btn_frame,
                image=self.delete_paper_button_icon,
                text="Remove SSC-II Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            remove_ssc_2_exam_btn.grid(row=0, column=3, padx=5, pady=5, sticky="we")

        # HSSC exams
        hssc_exams_frame = ctk.CTkFrame(content_frame, fg_color=bg)
        hssc_exams_frame.pack(side="top", fill="x", padx=(0, 0), pady=5)

        hssc_label = ctk.CTkLabel(
            hssc_exams_frame,
            text="HSSC Exams",
            text_color=text_fg,
            fg_color=bg,
            font=("Helvetica", 16, "bold")
        )
        hssc_label.pack(fill="x")

        # HSSC contents frame
        hssc_contents_frame = ctk.CTkFrame(hssc_exams_frame, fg_color=bg)
        hssc_contents_frame.pack(fill="x", padx=0, pady=0, expand="true")

        # HSSC-I
        hssc_1_frame = ctk.CTkFrame(hssc_contents_frame, fg_color=bg)
        hssc_1_frame.pack(side="top", fill="x", padx=(0, 0), pady=0, ipady=0)

        hssc_1_label = ctk.CTkLabel(
            hssc_1_frame,
            text="HSSC-I",
            text_color=text_fg,
        )
        hssc_1_label.pack(fill="x")

        # HSSC-I contents
        self.hssc_1_content_frame = ctk.CTkScrollableFrame(hssc_1_frame, fg_color=bg, orientation="horizontal")
        self.hssc_1_content_frame.pack(fill="x", padx=0, pady=0, ipady=0)

        # HSSC-II
        hssc_2_frame = ctk.CTkFrame(hssc_contents_frame, fg_color=bg)
        hssc_2_frame.pack(side="top", fill="x", padx=(0, 0), pady=0, ipady=0)

        hssc_2_label = ctk.CTkLabel(
            hssc_2_frame,
            text="HSSC-II",
            text_color=text_fg,
        )
        hssc_2_label.pack(fill="x")

        # HSSC-II contents
        self.hssc_2_content_frame = ctk.CTkScrollableFrame(hssc_2_frame, fg_color=bg, orientation="horizontal")
        self.hssc_2_content_frame.pack(fill="x", padx=0, pady=0, ipady=0)

        if self.role == "admin":
            # HSSC frame buttons
            hssc_current_exams_config_btn_frame = ctk.CTkFrame(hssc_contents_frame, fg_color=bg)
            hssc_current_exams_config_btn_frame.pack(side="top", fill="x", padx=(0, 0), pady=5)

            # Add HSSC-I Exam
            add_hssc_1_exam_btn = ctk.CTkButton(
                hssc_current_exams_config_btn_frame,
                image=self.add_exams_button_icon,
                text="Add HSSC-I Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            add_hssc_1_exam_btn.grid(row=0, column=0,padx=5, pady=5, sticky="we")

            # Remove HSSC-I Exam
            remove_hssc_1_exam_btn = ctk.CTkButton(
                hssc_current_exams_config_btn_frame,
                image=self.delete_paper_button_icon,
                text="Remove HSSC-I Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            remove_hssc_1_exam_btn.grid(row=0, column=1, padx=5, pady=5, sticky="we")

            # Add HSSC-II Exam
            add_hssc_2_exam_btn = ctk.CTkButton(
                hssc_current_exams_config_btn_frame,
                image=self.add_exams_button_icon,
                text="Add HSSC-II Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            add_hssc_2_exam_btn.grid(row=0, column=2, padx=5, pady=5, sticky="we")

            # Remove HSSC-II Exam
            remove_hssc_2_exam_btn = ctk.CTkButton(
                hssc_current_exams_config_btn_frame,
                image=self.delete_paper_button_icon,
                text="Remove HSSC-II Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            remove_hssc_2_exam_btn.grid(row=0, column=3, padx=5, pady=5, sticky="we")

        # About examinations frame
        about_exams_frame = ctk.CTkFrame(scrollable_frame, fg_color=bg)
        about_exams_frame.pack(fill="x", padx=(10, 10), pady=(20, 10))

        # Exams info title
        exams_info_label = ctk.CTkLabel(
            about_exams_frame,
            text="About Examinations",
            text_color=text_fg,
            fg_color=bg,
            font=("Helvetica", 22, "bold")
        )
        exams_info_label.pack(side="top", fill="x", pady=10)

        # Exams info content frame
        exams_info_content_frame = ctk.CTkFrame(about_exams_frame, fg_color=bg, bg_color=bg)
        exams_info_content_frame.pack(side="top", fill="x", pady=10)

        # Assessments info
        assessment_info_frame = ctk.CTkFrame(exams_info_content_frame, fg_color=bg, bg_color=bg)
        assessment_info_frame.grid(row=0, column=0, padx=2, pady=5, sticky="ew")

        title = ctk.CTkLabel(
            assessment_info_frame,
            text="Assessments:",
            text_color=text_fg,
            font=("Helvetica", 14, "bold")
        )
        title.grid(row=0, column=0, padx=0, pady=0, sticky="snew")

        text = ctk.CTkLabel(
            assessment_info_frame,
            text="\nAssessments are taken every month. It usually\n takes about a week to complete, one or two subjects per\n day, and about 30-40 minutes for every subject.\n\nTaken By: College\n Management: College\n Syllabus: Specific Chapters\n Duration: 1-2 weeks\n",
            fg_color=fg,
            bg_color=bg,
            text_color=text_fg,
            font=("Helvetica", 12)
        )
        text.grid(row=1, column=0, padx=0, pady=(0, 5), ipadx=8, sticky="snew")

        # Term exams
        term_info_frame = ctk.CTkFrame(exams_info_content_frame, fg_color=bg, bg_color=bg)
        term_info_frame.grid(row=0, column=1, padx=(16, 8), pady=5, sticky="ew")

        title = ctk.CTkLabel(
            term_info_frame,
            text="Terms:",
            bg_color=bg,
            text_color=text_fg,
            font=("Helvetica", 14, "bold")
        )
        title.grid(row=0, column=0, padx=0, pady=0, sticky="snew")

        text = ctk.CTkLabel(
            term_info_frame,
            text="\nTerm Examination is taken twice a year.\n 2-3 subjects every week, and about 2-3 hours for every\n subject and no classes happens during terms.\n\nTaken By: APSACS\n Management: College\n Syllabus: Half of the course\n Duration: 2-4 weeks\n",
            fg_color=fg,
            bg_color=bg,
            text_color=text_fg,
            font=("Helvetica", 12)
        )
        text.grid(row=1, column=0, padx=0, pady=(0, 5), ipadx=8, sticky="snew")

        # Standup or preboard
        preboard_info_frame = ctk.CTkFrame(exams_info_content_frame, fg_color=bg, bg_color=bg)
        preboard_info_frame.grid(row=0, column=2, padx=(8, 16), pady=5, sticky="ew")

        title = ctk.CTkLabel(
            preboard_info_frame,
            text="Pre-Board:",
            text_color=text_fg,
            bg_color=bg,
            font=("Helvetica", 14, "bold")
        )
        title.grid(row=0, column=0, padx=0, pady=0, sticky="snew")

        text = ctk.CTkLabel(
            preboard_info_frame,
            text="\nPre-Board Exam is taken after 2nd term. Its\n managements and timings are same as term exams,\n and classes are also not takes place. \n\nTaken By: APSACS\n Management: College\n Syllabus: Everything\n Duration: 2-4 weeks\n",
            fg_color=fg,
            text_color=text_fg,
            bg_color=bg,
            font=("Helvetica", 12)
        )
        text.grid(row=1, column=0, padx=0, pady=(0, 5), ipadx=8, sticky="snew")

        # Finale
        final_info_frame = ctk.CTkFrame(exams_info_content_frame, fg_color=bg, bg_color=bg)
        final_info_frame.grid(row=0, column=3, padx=2, pady=5, sticky="ew")

        title = ctk.CTkLabel(
            final_info_frame,
            text="Annual Examinations:",
            text_color=text_fg,
            bg_color=bg,
            font=("Helvetica", 14, "bold")
        )
        title.grid(row=0, column=0, padx=0, pady=0, sticky="snew")

        text = ctk.CTkLabel(
            final_info_frame,
            text="\nAnnual Examinations are taken at the end of\n the year. It has the most importance and student are\n promoted to the next class if passed. \n\nTaken By: FBISE(board)\n Management: FBISE(board)\n Syllabus: Everything\n Duration: 1 month\n",
            fg_color=fg,
            bg_color=bg,
            text_color=text_fg,
            font=("Helvetica", 12)
        )
        text.grid(row=1, column=0, padx=0, pady=(0, 5), ipadx=8, sticky="snew")


        subject_icon_map = {
            "Physics": phy_icon,
            "Chemistry": chem_icon,
            "Biology": bio_icon,
            "Computer Science": cs_icon,
            "Islamiyat": isl_icon,
            "Mathematics": math_icon,
            "Urdu": urdu_icon,
            "Pakistan Studies": ps_icon,
            "English": eng_icon
        }

        def load_subjects(file_path):
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    return data.get("subjects", [])
            except json.JSONDecodeError:
                print(f"Error: The file {file_path} is not a valid JSON file or is empty.")
                return []
            except FileNotFoundError:
                print(f"Error: The file {file_path} was not found.")
                return []

        default_icon = phy_icon

        def create_subject_frame(parent_frame, subject_data):
            subject_name = subject_data["subject_name"]
            icon = subject_icon_map.get(subject_name, default_icon)

            sub_frame = ctk.CTkFrame(parent_frame, fg_color=fg)
            sub_frame.pack(side="left", padx=5, pady=5)

            sub_icon = ctk.CTkLabel(sub_frame, text="", image=icon, height=80, width=80)
            sub_icon.grid(row=0, column=0, rowspan=3, padx=(10, 0), pady=10)

            sub_text = ctk.CTkLabel(
                sub_frame,
                text=subject_name,
                text_color=text_fg,
                font=("Helvetica", 16)
            )
            sub_text.grid(row=0, column=1, padx=5, pady=(5, 0))

            sub_sub_text = ctk.CTkLabel(
                sub_frame,
                text=f"Date: {subject_data['date']}\nDay: {subject_data['day']}\nTime: {subject_data['time']}\nExamination: {subject_data['Examination']}",
                text_color=text_fg,
                font=("Helvetica", 12)
            )
            sub_sub_text.grid(row=1, column=1, padx=5, ipadx=2, pady=(0, 5))

        ssc1_subjects = load_subjects(f"{base_path}/json/ssc1_exams.json")
        ssc2_subjects = load_subjects(f"{base_path}/json/ssc2_exams.json")
        hssc1_subjects = load_subjects(f"{base_path}/json/hssc1_exams.json")
        hssc2_subjects = load_subjects(f"{base_path}/json/hssc2_exams.json")

        if not ssc1_subjects:
            ssc1_label = ctk.CTkLabel(self.ssc_1_content_frame, text="No ongoing exams", font=("Helvetica", 16, "bold"), text_color=text_fg)
            ssc1_label.pack(fill="x", pady=50)
        else:
            for subject in ssc1_subjects:
                create_subject_frame(self.ssc_1_content_frame, subject)

        if not ssc2_subjects:
            ssc2_label = ctk.CTkLabel(self.ssc_2_content_frame, text="No ongoing exams", font=("Helvetica", 16, "bold"), text_color=text_fg)
            ssc2_label.pack(fill="x", pady=50)
        else:
            for subject in ssc2_subjects:
                create_subject_frame(self.ssc_2_content_frame, subject)

        if not hssc1_subjects:
            hssc1_label = ctk.CTkLabel(self.hssc_1_content_frame, text="No ongoing exams", font=("Helvetica", 16, "bold"), text_color=text_fg)
            hssc1_label.pack(fill="x", pady=50)
        else:
            for subject in hssc1_subjects:
                create_subject_frame(self.hssc_1_content_frame, subject)

        if not hssc2_subjects:
            hssc2_label = ctk.CTkLabel(self.hssc_2_content_frame, text="No ongoing exams", font=("Helvetica", 16, "bold"), text_color=text_fg)
            hssc2_label.pack(fill="x", pady=50)
        else:
            for subject in hssc2_subjects:
                create_subject_frame(self.hssc_2_content_frame, subject)

    def show_results(self):
        # clears the main frame and sets the button state
        self.clear_main_frame()
        self.set_button_state(self.results_button)

        # Main frame
        self.results_main_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=bg,
            bg_color=bg
        )
        self.results_main_frame.pack(fill="both", expand="true", padx=10, pady=10)

        exam_name: str = "Annual Examinations HSSC 2024 Results"

        self.exam_name = ctk.CTkLabel(
            self.results_main_frame,
            fg_color=bg,
            font=("helvetica", 22, "bold"),
            text=exam_name,
            text_color=text_fg
        )
        self.exam_name.pack(side="top", fill="x", padx=5, pady=5)

        # Search frame
        self.search_frame = ctk.CTkFrame(self.results_main_frame, fg_color=bg)
        self.search_frame.pack(side="top", fill="x", padx=500, pady=5)

        self.search_btn = ctk.CTkButton(
            self.search_frame,
            text="Search",
            width=100,
            fg_color=btn_active,
            hover_color=btn_hvr
        )
        self.search_btn.pack(side="right", padx=5, pady=5)

        self.roll_no_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Enter roll number...", width=300)
        self.roll_no_entry.pack(side="right", padx=5, pady=5)

        self.result_content_frame = ctk.CTkFrame(self.results_main_frame, fg_color=bg)
        self.result_content_frame.pack(side="top", fill="both", padx=5, pady=5, expand=True)

    def show_papers(self):
        # Clear the main frame and set the button state
        self.clear_main_frame()
        self.set_button_state(self.papers_button)

        # Main scrollable frame
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color=bg,
            bg_color=bg
        )
        self.scrollable_frame.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")

        # Buttons frame
        self.button_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=bg
        )
        self.button_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

        # Refresh papers button
        refresh_pdfs_button = ctk.CTkButton(
            self.button_frame,
            text="Refresh Papers",
            text_color=text_fg_2,
            image=self.refresh_pdfs_button_icon,
            fg_color=btn_active,
            hover_color=btn_hvr,
            command=self.refresh_pdfs
        )
        refresh_pdfs_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Add papers button
        add_paper_button = ctk.CTkButton(
            self.button_frame,
            text="Add Papers",
            text_color=text_fg_2,
            image=self.add_paper_button_icon,
            hover_color=btn_hvr,
            fg_color=btn_active,
            command=self.add_paper
        )
        add_paper_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Delete papers button
        delete_paper_button = ctk.CTkButton(
            self.button_frame,
            text="Remove Papers",
            text_color=text_fg_2,
            image=self.delete_paper_button_icon,
            hover_color=btn_hvr,
            fg_color=btn_active,
            command=self.delete_paper
        )
        delete_paper_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Main frame configurations
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Load the pdfs to the main scrollable frame
        self.load_pdfs(DEFAULT_PDFs_PATH)

# helper functions for show home section
    def logout(self):
        raise NotImplementedError

    def show_edit_news(self):
        # Edit news window initialization
        self.edt_news_window = ctk.CTk()

        # Window configuration
        self.edt_news_window.geometry("800x300")

        self.title = ctk.CTkLabel(
            self.edt_news_window,
            text="Edit the News",
            font=("Helvetica", 22, "bold"),
            fg_color=bg,
            text_color=text_fg
        )
        self.title.pack(fill="x", side="top")

        # Main frame
        self.main_frame = ctk.CTkFrame(self.edt_news_window, fg_color=bg, corner_radius=0)
        self.main_frame.pack(fill="x")

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

        # news 4
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
        self.save_button.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        self.cancel_button = ctk.CTkButton(
            self.main_frame,
            text="Cancel",
            text_color=text_fg_2,
            fg_color=btn_active,
            bg_color=bg,
            hover_color=btn_hvr,
            command=self.edt_news_window.destroy
        )
        self.cancel_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.edt_news_window.mainloop()

    def save_news(self):
        # Save the news entries
        self.news_1 = self.news_1_entry.get()
        self.news_2 = self.news_2_entry.get()
        self.news_3 = self.news_3_entry.get()
        self.news_4 = self.news_4_entry.get()

        # Write the news to the file
        with open(f"{base_path}\news.txt", "w") as f:
            f.truncate(0)
            f.write(f"{self.news_1}\n{self.news_2}\n{self.news_3}\n{self.news_4}")
            print("News updated successfully!")

        # Close the window
        self.edt_news_window.destroy()

    def show_contact_us(self):
        """Show contact information on a different window."""

        # Create a new window for showing contact information
        self.show_contact_us_window = ctk.CTk()
        self.show_contact_us_window.overrideredirect(True)

        WIDTH = 400
        HEIGHT = 250

        # Place the window in the center of the screen and make it draggable
        self.center_window(self.show_contact_us_window)
        self.make_window_draggable(self.show_contact_us_window)

        # Create a frame for holding the contact information
        main_frame1 = ctk.CTkFrame(
            self.show_contact_us_window,
            width=WIDTH,
            height=HEIGHT,
            fg_color=fg,
            corner_radius=0,
            border_width=2,
            border_color=text_fg
        )
        main_frame1.grid(padx=10, pady=10)

        # Add a title label to the frame
        title = ctk.CTkLabel(
            main_frame1,
            text="Contact Us",
            text_color=text_fg,
            font=("Helvetica", 22, "bold")
        )
        title.pack(side="top", fill="x", padx=10, pady=5)

        # Add a label with contact information to the frame
        info = ctk.CTkLabel(
            main_frame1,
            text="For any queries, please contact us at:\n\nEmail: balgharisaifullah@gmail.com\nPhone: +92355-4300937",
            text_color=text_fg,
            font=("Helvetica", 16)
        )
        info.pack(side="top", fill="x", expand=True, padx=10, pady=10)

        # Add a close button to the frame to close the window when clicked
        close_button = ctk.CTkButton(
            main_frame1,
            text="Close",
            text_color=text_fg_2,
            font=("Helvetica", 14),
            fg_color=btn_active,
            hover_color=btn_hvr,
            command=self.show_contact_us_window.destroy
        )
        close_button.pack(side="top", fill="x", padx=50, pady=10)

        # Run the mainloop
        self.show_contact_us_window.mainloop()

    def center_window(self, window, width=300, height=200):
        """Center the window on the screen."""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")

    def make_window_draggable(self, window):
        """Make the window draggable by clicking and dragging it with the mouse."""
        def start_drag(event):
            window.x = event.x
            window.y = event.y

        def drag(event):
            x = window.winfo_pointerx() - window.x
            y = window.winfo_pointery() - window.y
            window.geometry(f"+{x}+{y}")

        window.bind("<Button-1>", start_drag)
        window.bind("<B1-Motion>", drag)

# helper functions for show examinations section
    def get_exams_info(self):
        raise NotImplementedError

# helper functions for show papers section
    def refresh_pdfs(self):
        self.load_pdfs(DEFAULT_PDFs_PATH)

    def add_paper(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            dest_path = os.path.join(DEFAULT_PDFs_PATH, os.path.basename(pdf_path))
            if not os.path.exists(dest_path):
                shutil.copy(pdf_path, dest_path)
            self.load_pdfs(DEFAULT_PDFs_PATH)

    def delete_paper(self):
        pdf_path = filedialog.askopenfilename(initialdir=DEFAULT_PDFs_PATH, filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            os.remove(pdf_path)
            self.load_pdfs(DEFAULT_PDFs_PATH)

    def get_pdf_thumbnail(self, pdf_path, size=(100, 150)):
        try:
            cache_file_name = os.path.splitext(os.path.basename(pdf_path))[0] + ".png"
            cache_file_path = os.path.join(CACHE_FOLDER_PATH, cache_file_name)

            if os.path.exists(cache_file_path):
                pdf_mtime = os.path.getmtime(pdf_path)
                cache_mtime = os.path.getmtime(cache_file_path)
                if pdf_mtime <= cache_mtime:
                    return Image.open(cache_file_path)

            pages = convert_from_path(pdf_path, first_page=1, last_page=1, size=size)
            if pages:
                img = pages[0]
                img.thumbnail(size, Image.LANCZOS)
                img.save(cache_file_path)
                return img
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load PDF: {e}")
            return None

    def add_pdf_tile(self, frame, pdf_path, row, col, width=230):
        thumbnail = self.get_pdf_thumbnail(pdf_path)
        if thumbnail:
            img_tk = ImageTk.PhotoImage(thumbnail)

            tile_frame = ctk.CTkFrame(frame, width=width, height=250, fg_color=fg)
            tile_frame.grid(row=row, column=col, padx=10, pady=10)
            tile_frame.grid_propagate(False)

            label_image = ctk.CTkLabel(tile_frame, image=img_tk, text="", text_color=text_fg)
            # label_image.image = img_tk
            label_image.pack(pady=15, padx=20)

            file_name = os.path.basename(pdf_path)
            if len(file_name) > 15:
                file_name = file_name[:15] + "..."
            label_text = ctk.CTkLabel(tile_frame, text=file_name)
            label_text.pack()

            tile_frame.bind("<Button-1>", lambda e, path=pdf_path: self.open_pdf(path))

    def open_pdf(self, pdf_path):
        try:
            if platform.system() == "Linux":
                os.system(f"xdg-open \"{pdf_path}\"")
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open \"{pdf_path}\"")
            elif platform.system() == "Windows":
                os.system(f"start \"\" \"{pdf_path}\"")
            else:
                messagebox.showerror("Error", "Unsupported OS")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open PDF: {e}")

    def load_pdfs(self, directory):
        try:
            self.scrollable_frame.destroy()
            self.scrollable_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color=bg)
            self.scrollable_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
            if not pdf_files:
                messagebox.showinfo("Info", "No PDF files found in the directory.")
                return

            row = 0
            col = 0
            max_columns = 8
            for i, pdf_file in enumerate(pdf_files):
                pdf_path = os.path.join(directory, pdf_file)
                self.add_pdf_tile(self.scrollable_frame, pdf_path, row, col)
                col += 1
                if col >= max_columns:
                    col = 0
                    row += 1
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load PDFs: {e}")

    def clear_main_frame(self):

        for widget in self.main_frame.winfo_children():
            widget.destroy()

