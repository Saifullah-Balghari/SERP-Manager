# Disclaimer:
# Icons are not designed by me, sourced from www.flaticon.com

# This is a simple GUI Application that can be used as an Examinations, Results and Paper Manager.
# As of now this project is a personal side project and is not intended for commercial use or distribution.

# External imports
import customtkinter as ctk
from tkinter import messagebox, filedialog      # tk
from pdf2image import convert_from_path
from PIL import Image, ImageTk                  # pillow

# Local imports
from . import contact_us
from . import manage_news
from . import show_profile
from .settings import *

# Inbuilt imports
import platform
import json
import shutil
import os
import warnings

warnings.filterwarnings("ignore", 
                        message="CTkLabel Warning: Given image is not CTkImage but",
                        module="customtkinter")

# Default settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

class SERPManagerGUI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        try:
            if not os.path.exists(cache_folder_path):
                os.makedirs(cache_folder_path)

            # Variables declarations
            self.selected_button = None
            self.role = "student"

            # Load the current role from the file
            with open(current_role_path, 'r') as f:
                text = f.read()        
                self.username, self.role = text.split()
                self.role = self.role.lower().strip()

                if self.role not in ["student", "admin"]:
                    raise ValueError("Invalid role")

            try:               
                # Loads the icons
                setup_icons()

                # Window configurations
                self.title("SERP-Manager (Developed By Saifullah Balghari)")
                self.geometry("1366x768")
                self.resizable(False, False)
                self.configure(fg_color=text_fg)   
                self.iconbitmap(None, None)
                self.grid_rowconfigure(0, weight=1) 
                self.grid_rowconfigure(1, weight=15)
                self.grid_columnconfigure(0, weight=1)

                # Create the header frame
                self.create_header_frame()

                # Create the main frame
                self.create_main_frame()

                # Run the main loop
                self.mainloop()

            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            # Remove the current role file after closing the main GUI window
            os.remove(current_role_path)

    def create_header_frame(self):

        # Create the header frame
        self.header_frame = ctk.CTkFrame(self, fg_color=bg, corner_radius=0)
        self.header_frame.pack(padx=0, pady=(0, 1), side="top", fill="x", ipadx=10, ipady=10)

        # Header frame configuration
        self.header_frame.pack_propagate(False)         
        self.header_frame.configure(height=40)

        # Create the button frame
        button_frame = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        button_frame.pack(padx=10, pady=(10, 0), side="top", fill="x")

        # Home button
        self.home_button = ctk.CTkButton(
            button_frame,
            text="Home",
            text_color=text_fg,
            width=80,
            height=30,
            font=("Helvetica", 18, "bold"),
            hover_color=btn_hvr,
            anchor="center",
            command=self.show_home
        )
        self.home_button.pack(padx=10, pady=5, side="left")

        # Exams button
        self.exams_button = ctk.CTkButton(
            button_frame,
            text="Exams",
            width=80,
            image=exam_button_icon,
            height=30,
            font=("Helvetica", 18, "bold"),
            hover_color=btn_hvr,
            text_color=text_fg,
            anchor="center",
            command=self.show_examinations
        )
        self.exams_button.pack(padx=0, pady=5, side="left")

        # Results button
        self.results_button = ctk.CTkButton(
            button_frame,
            text="Results",
            image=result_button_icon,
            width=80,
            height=30,
            font=("Helvetica", 18, "bold"),
            hover_color=btn_hvr,
            anchor="center",
            text_color=text_fg,
            command=self.show_results                           
        )
        self.results_button.pack(padx=(10,0), pady=5, side="left")

        # Papers button
        self.papers_button = ctk.CTkButton(
            button_frame,
            text="Papers",
            image=paper_button_icon,
            width=80,
            height=30,
            font=("Helvetica", 18, "bold"),
            hover_color=btn_hvr,                            
            anchor="center",
            text_color=text_fg,
            command=self.show_papers
        )
        self.papers_button.pack(padx=10, pady=5, side="left")

        # Profile button
        self.profile_button = ctk.CTkButton(
            button_frame,
            text=self.username,
            image=acc_button_icon,
            font=("Helvetica", 18, "bold"),
            hover_color=fg,
            width=80,
            height=30,
            anchor="center",
            fg_color="transparent",
            text_color=text_fg,
            command=self.show_profile
        )
        self.profile_button.pack(padx=10, pady=5, side="right")
        
        self.show_profile_toplevel_window = None

    def create_main_frame(self):

        # Create the main frame
        self.main_frame = ctk.CTkFrame(self, fg_color=bg, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        self.main_frame.pack_propagate(False)

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
        wellcome_message_frame = ctk.CTkFrame(self.main_frame, height=60, fg_color=bg)
        wellcome_message_frame.pack(side="top", fill="x", padx=5, pady=(0, 0))

        # Title Label
        logo_label = ctk.CTkLabel(
            wellcome_message_frame,
            text="Welcome To SERP-Manager",
            text_color=text_fg,
            font=("Helvetica", 30, "bold")
                 )
        logo_label.pack(side="top", fill="x")

        # Introduction Label
        intro_label = ctk.CTkLabel(
            wellcome_message_frame,
            text="Manage examinations, results, and much more...",
            text_color=text_fg,
            font=("Helvetica", 14)
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
        shortcut_1_frame.grid(row=0, column=0, padx=28, pady=10, sticky="nsew")

        shortcut_1_icon = ctk.CTkLabel(shortcut_1_frame, text="", image=icons["shortcut_1_icon"], height=120, width=120)
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
        shortcut_2_frame.grid(row=0, column=1, padx=28, pady=10, sticky="nsew")

        shortcut_2_icon = ctk.CTkLabel(
            shortcut_2_frame,
            text="",
            image=icons["shortcut_2_icon"],
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
            text="Stay up to date with ongoing\n examination's datesheets. Teachers will be \nableto change, remove or add exams.",
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
        shortcut_3_frame.grid(row=0, column=2, padx=28          , pady=10, sticky="nsew")

        shortcut_3_icon = ctk.CTkLabel(shortcut_3_frame, text="", image=icons["shortcut_3_icon"], height=120, width=120)
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

        title_frame = ctk.CTkFrame(news_n_updates, fg_color=bg, bg_color=bg)
        title_frame.pack(side="top", fill="x", padx=10, pady=0)

        news_icon = ctk.CTkLabel(
            title_frame,
            text="",
            image=icons["news_icon"],
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

        with open(news_txt_path, "rb") as f:
            lines = f.readlines()

        self.news_1 = lines[0].strip() if len(lines) > 0 else ""
        self.news_2 = lines[1].strip() if len(lines) > 1 else ""
        self.news_3 = lines[2].strip() if len(lines) > 2 else ""
        self.news_4 = lines[3].strip() if len(lines) > 3 else ""

        # news 1
        news_1_frame = ctk.CTkFrame(news_frame, fg_color=fg)
        news_1_frame.pack(fill="x", padx=0, pady=(0, 2))

        news_arrow = ctk.CTkLabel(
            news_1_frame,
            image=icons["arrow_icon"],
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
            image=icons["arrow_icon"],
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
            image=icons["arrow_icon"],
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
            image=icons["arrow_icon"],
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

        role_1_icon = ctk.CTkLabel(role_1_frame, text="", image=icons["role_1_icon"], height=120, width=120)
        role_1_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        role_1_text = ctk.CTkLabel(
            role_1_frame,
            text="Admins",
            text_color=text_fg,
            font=("Helvetica", 18)
        )
        role_1_text.grid(row=0, column=1, padx=8, pady=(10, 0))

        role_1_sub_text = ctk.CTkLabel(
            role_1_frame,
            text="This role is for the staff of the school.\n They will have access to all features, they\n will be able to add, edit or remove\n exams, results and papers.",
            text_color=text_fg,
            font=("Helvetica", 13)
        )
        role_1_sub_text.grid(row=1, column=1, padx=8, pady=0)

        # student role
        role_2_frame = ctk.CTkFrame(about_roles_and_us, fg_color=fg)
        role_2_frame.grid(row=0, column=1, padx=8, pady=20, sticky="nsew")

        role_2_icon = ctk.CTkLabel(role_2_frame, text="", image=icons["role_2_icon"], height=120, width=120)
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
        help_frame.grid(row=0, column=2, padx=8, pady=20, sticky="nsew")

        about_us_icon = ctk.CTkLabel(help_frame, text="", image=icons["help_icon"], height=120, width=120)
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
        buttons_frame.pack(side="bottom", fill="x", padx=0, pady=0, ipady=0)

        # close button
        close_btn = ctk.CTkButton(
            buttons_frame,
            text="Close",
            text_color=text_fg,
            hover_color=btn_hvr,
            border_width=1,
            border_color=text_fg,
            fg_color=bg,
            command=self.destroy
        )
        close_btn.pack(side="right", padx=5, pady=5)

        # Contact us button
        contact_us_button = ctk.CTkButton(
            buttons_frame,
            text="Contact Us",
            command=self.contact_us_toplevel,
            text_color=text_fg_2,
            hover_color=btn_hvr,
            image=contact_us_button_icon,
            fg_color=btn_active,
        )
        contact_us_button.pack(side="left", padx=5, pady=5)

        self.contact_us_toplevel_window = None

        if self.role == "admin":
            # Edit news button
            add_news_button = ctk.CTkButton(
                buttons_frame,
                text="Edit News",
                command=self.manage_news_toplevel,
                text_color=text_fg_2,
                image=edit_button_icon,
                hover_color=btn_hvr,
                fg_color=btn_active,
            )
            add_news_button.pack(side="left", padx=5, pady=5)

            self.manage_news_toplevel_window = None

        # Refresh button
        refresh_button = ctk.CTkButton(
            buttons_frame,
            text="Refresh",
            image=refresh_pdfs_button_icon,
            command=self.show_home,
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

        # Create the scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color=bg
        )
        scrollable_frame.pack(fill="both", expand=True, side="top", pady=0)

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
        current_exams_label.pack(fill="x", padx=10, pady=0, ipady=0)

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

            # Edit Exam Buttons frame
            edit_exam_btn_frame = ctk.CTkFrame(self.main_frame, fg_color=bg)
            edit_exam_btn_frame.pack(side="bottom", fill="x", padx=20, pady=0)

            # Add SSC-I Exam
            add_ssc_1_exam_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=add_exams_button_icon,
                text="Edit SSC-I Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            add_ssc_1_exam_btn.grid(row=0, column=0,padx=5, pady=(0, 5), sticky="we")

            # Remove SSC-I Exam
            remove_ssc_1_exam_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=delete_paper_button_icon,
                text="Remove SSC-I Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            remove_ssc_1_exam_btn.grid(row=0, column=1, padx=5, pady=(0, 5), sticky="we")

            # Add SSC-II Exam
            add_ssc_2_exam_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=add_exams_button_icon,
                text="Edit SSC-II Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            add_ssc_2_exam_btn.grid(row=0, column=2, padx=5, pady=(0, 5), sticky="we")

            # Remove SSC-II Exam
            remove_ssc_2_exam_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=delete_paper_button_icon,
                text="Remove SSC-II Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            remove_ssc_2_exam_btn.grid(row=0, column=3, padx=5, pady=(0, 5), sticky="we")

            # Add HSSC-I Exam
            add_hssc_1_exam_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=add_exams_button_icon,
                text="Add HSSC-I Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            add_hssc_1_exam_btn.grid(row=0, column=4,padx=5, pady=(0, 5), sticky="we")

            # Remove HSSC-I Exam
            remove_hssc_1_exam_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=delete_paper_button_icon,
                text="Remove HSSC-I Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            remove_hssc_1_exam_btn.grid(row=0, column=5, padx=5, pady=(0, 5), sticky="we")

            # Add HSSC-II Exam
            add_hssc_2_exam_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=add_exams_button_icon,
                text="Add HSSC-II Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            add_hssc_2_exam_btn.grid(row=0, column=6, padx=5, pady=(0, 5), sticky="we")

            # Remove HSSC-II Exam
            remove_hssc_2_exam_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=delete_paper_button_icon,
                text="Remove HSSC-II Exam",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr
            )
            remove_hssc_2_exam_btn.grid(row=0, column=7, padx=5, pady=(0, 5), sticky="we")

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
        
        # Loads subject's icons respectively
        subject_icon_map = {
            "Physics": icons["phy_icon"],
            "Chemistry": icons["chem_icon"],
            "Biology": icons["bio_icon"],
            "Computer Science": icons["cs_icon"],
            "Islamiyat": icons["isl_icon"],
            "Mathematics": icons["math_icon"],
            "Urdu": icons["urdu_icon"],
            "Pakistan Studies": icons["ps_icon"],
            "English": icons["eng_icon"]
        }

        def create_subject_frame(parent_frame, subject_data):
            subject_name = subject_data["subject_name"]

            icon = subject_icon_map.get(subject_name, icons.get("default_icon"))

            sub_frame = ctk.CTkFrame(parent_frame, fg_color=fg)         
            sub_frame.pack(side="left", padx=5, pady=0)

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

        ssc1_subjects = load_subjects(ssc1_json_path)
        ssc2_subjects = load_subjects(ssc2_json_path)
        hssc1_subjects = load_subjects(hssc1_json_path)
        hssc2_subjects = load_subjects(hssc2_json_path)

        if not ssc1_subjects:
            ssc1_label = ctk.CTkLabel(self.ssc_1_content_frame, text="No ongoing exams", font=("Helvetica", 18), text_color=text_fg)
            ssc1_label.pack(fill="x", pady=50)
        else:
            for subject in ssc1_subjects:
                create_subject_frame(self.ssc_1_content_frame, subject)

        if not ssc2_subjects:
            ssc2_label = ctk.CTkLabel(self.ssc_2_content_frame, text="No ongoing exams", font=("Helvetica", 18), text_color=text_fg)
            ssc2_label.pack(fill="x", pady=50)
        else:
            for subject in ssc2_subjects:
                create_subject_frame(self.ssc_2_content_frame, subject)

        if not hssc1_subjects:
            hssc1_label = ctk.CTkLabel(self.hssc_1_content_frame, text="No ongoing exams", font=("Helvetica", 18), text_color=text_fg)
            hssc1_label.pack(fill="x", pady=50)
        else:
            for subject in hssc1_subjects:
                create_subject_frame(self.hssc_1_content_frame, subject)

        if not hssc2_subjects:
            hssc2_label = ctk.CTkLabel(self.hssc_2_content_frame, text="No ongoing exams", font=("Helvetica", 18), text_color=text_fg)
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
        self.results_main_frame.pack(fill="both", expand="true", padx=0, pady=0)

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

        self.result_content_frame = ctk.CTkFrame(self.results_main_frame, fg_color=fg)
        self.result_content_frame.pack(side="top", fill="both", padx=10, pady=10, expand=True)

    def show_papers(self):
        # Clear the main frame and set the button state
        self.clear_main_frame()
        self.set_button_state(self.papers_button)

        # Buttons frame
        self.button_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=bg
        )
        self.button_frame.pack(side="bottom", fill="x", padx=0, pady=0, ipady=0)

        # Refresh papers button
        refresh_pdfs_button = ctk.CTkButton(
            self.button_frame,
            text="Refresh Papers",
            text_color=text_fg_2,
            image=refresh_pdfs_button_icon,
            fg_color=btn_active,
            hover_color=btn_hvr,
            command=self.refresh_pdfs
        )
        refresh_pdfs_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Add papers button
        add_paper_button = ctk.CTkButton(
            self.button_frame,
            text="Add Papers",
            text_color=text_fg_2,
            image=add_paper_button_icon,
            hover_color=btn_hvr,
            fg_color=btn_active,
            command=self.add_paper
        )
        add_paper_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Delete papers button
        delete_paper_button = ctk.CTkButton(
            self.button_frame,
            text="Remove Papers",
            text_color=text_fg_2,
            image=delete_paper_button_icon,
            hover_color=btn_hvr,
            fg_color=btn_active,
            command=self.delete_paper
        )
        delete_paper_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Main frame configurations
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Load the pdfs to the main scrollable frame
        self.load_pdfs(default_pdfs_path)

    def show_profile(self):
        if self.show_profile_toplevel_window is None or not self.show_profile_toplevel_window.winfo_exists():
            self.show_profile_toplevel_window = show_profile.CurrentAccount(self)
        else:
            self.show_profile_toplevel_window.focus()

# helper function for show home section
    def contact_us_toplevel(self):
        if self.contact_us_toplevel_window is None or not self.contact_us_toplevel_window.winfo_exists():
            self.contact_us_toplevel_window = contact_us.ContactUs(self)
        else:
            self.contact_us_toplevel_window.focus()

    def manage_news_toplevel(self):
        if self.manage_news_toplevel_window is None or not self.manage_news_toplevel_window.winfo_exists():
            self.manage_news_toplevel_window = manage_news.ManageNews(self)
        else:
            self.manage_news_toplevel_window.focus()

# helper functions for show papers section
    def refresh_pdfs(self):
        self.show_papers()

    def add_paper(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            dest_path = os.path.join(default_pdfs_path, os.path.basename(pdf_path))
            if not os.path.exists(dest_path):
                shutil.copy(pdf_path, dest_path)
            self.load_pdfs(default_pdfs_path)

    def delete_paper(self):
        pdf_path = filedialog.askopenfilename(initialdir=default_pdfs_path, filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            os.remove(pdf_path)
            self.load_pdfs(default_pdfs_path)

    def get_pdf_thumbnail(self, pdf_path, size=(100, 150)):
        try:
            cache_file_name = os.path.splitext(os.path.basename(pdf_path))[0] + ".png"
            cache_file_path = os.path.join(cache_folder_path, cache_file_name)

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
            print(e)
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
            print(e)

    def load_pdfs(self, directory):
        try:
            self.scrollable_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color=bg)
            self.scrollable_frame.pack(side="top", fill="both", padx=0, pady=0, expand=True)

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
            print(e)

    def clear_main_frame(self):

        for widget in self.main_frame.winfo_children():
            widget.destroy()
