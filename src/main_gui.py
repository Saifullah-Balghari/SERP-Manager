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
from .toplevels import contact_us
from .toplevels import manage_news
from .toplevels import show_profile
from .toplevels import manage_exams
from .toplevels import show_student
from .toplevels import show_results
from .components.results import get_results
from .components.examination import datesheet
from .helpers import accounts
from .settings import *

# Inbuilt imports
import platform
import shutil
import os

# Default settings for ctk
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
            self.role = ""

            # Load the current role from the file
            with open(current_role_path, 'r') as f:
                text = f.read()        
                self.username, self.password = text.split()

            account = accounts.get_account(self.username, self.password)
            self.role = account['role'].lower()                     

            try:               
                # Loads the icons
                setup_icons()

                # Window configurations
                self.title("SERP - Developed By Saifullah Balghari")
                self.geometry("1366x768")
                self.resizable(1, 1)
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
        self.sidebar_frame = ctk.CTkFrame(self, fg_color=btn_active, corner_radius=0)
        self.sidebar_frame.pack(fill="y", side="left", padx=0, pady=0)

        # Sidebar frame configuration
        self.sidebar_frame.pack_propagate(False)         
        self.sidebar_frame.configure(width=200)

        logo_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="S E R P",
            text_color=text_fg_2,
            font=("Kumar One Outline", -42)
        )
        logo_label.pack(padx=5, pady=(10, 100),side="top", fill="x")

        # Home button
        self.home_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Home",
            text_color=text_fg,
            image=home_button_icon,
            font=("Helvetica", -14,),
            hover_color=btn_hvr,
            anchor="w",
            command=self.show_home
        )
        self.home_button.pack(padx=30, pady=10, fill="x")

        # Students button
        self.student_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Students",
            text_color=text_fg,
            image=students_button_icon,
            font=("Helvetica", -14,),
            hover_color=btn_hvr,
            anchor="w",
            command=self.show_students
        )
        self.student_button.pack(padx=30, pady=10, fill="x")

        # Exams button
        self.exams_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Exams",
            image=exam_button_icon,
            font=("Helvetica", -14,),
            hover_color=btn_hvr,
            text_color=text_fg,
            anchor="w",
            command=self.show_examinations
        )
        self.exams_button.pack(padx=30, pady=10, fill="x")

        # Results button
        self.results_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Results",
            image=result_button_icon,
            font=("Helvetica", -14,),
            hover_color=btn_hvr,
            anchor="w",            
            text_color=text_fg,
            command=self.show_results                           
        )
        self.results_button.pack(padx=30, pady=10, fill="x")

        # Papers button
        self.papers_button = ctk.CTkButton(
            self.sidebar_frame,
            text="Papers",
            image=paper_button_icon,
            font=("Helvetica", -14,),
            hover_color=btn_hvr,         
            anchor="w",
            text_color=text_fg,
            command=self.show_papers
        )
        self.papers_button.pack(padx=30, pady=10, fill="x")

        # Profile button
        self.profile_button = ctk.CTkButton(
            self.sidebar_frame,
            text=self.username,
            image=acc_button_icon,
            font=("Helvetica", -14),
            hover_color=btn_hvr,
            anchor="w", 
            fg_color=btn_active,
            text_color=text_fg_2,
            command=self.show_profile
        )
        self.profile_button.pack(padx=30, pady=20, side="bottom", fill="x")
        
        self.show_profile_toplevel_window = None

    def create_main_frame(self):

        # Create the main frame
        self.main_frame = ctk.CTkFrame(self, fg_color=bg, corner_radius=0)
        self.main_frame.pack(fill="both", expand="true", padx=0, pady=0, side="right")
        self.main_frame.pack_propagate(False)

        # Set the home section as the main frame
        self.show_home()

    def set_button_state(self, selected_button):

        # Reset the button state
        for button in [self.home_button, self.exams_button, self.results_button, self.papers_button, self.student_button]:
            button.configure(fg_color=btn_active, text_color=text_fg_2)

        # Set the selected button state
        selected_button.configure(text_color=text_fg, fg_color=fg)

# main sections
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

        # Main Scrollable Frame
        main_scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame, 
            fg_color=bg,
            scrollbar_button_color=btn_active, 
            scrollbar_button_hover_color=btn_hvr, 
            )
        main_scrollable_frame.pack(fill="both", expand="true", padx=5, pady=5)

        # Wellcome message frame
        wellcome_message_frame = ctk.CTkFrame(main_scrollable_frame, height=60, fg_color=bg)
        wellcome_message_frame.pack(side="top", fill="x", padx=5, pady=5)

        # Title Label
        logo_label = ctk.CTkLabel(
            wellcome_message_frame,
            text="Welcome To SERP-Manager",
            text_color=text_fg,
            font=("Helvetica", -32, "bold")
        )
        logo_label.pack(side="top", fill="x")

        # Introduction Label
        intro_label = ctk.CTkLabel(
            wellcome_message_frame,
            text="Manage examinations, results, and much more...",
            text_color="grey",
            font=("Helvetica", -14)
        )
        intro_label.pack(side="top", fill="x")

        # news and updates frame
        news_n_updates = ctk.CTkFrame(main_scrollable_frame, fg_color=bg)
        news_n_updates.pack(fill="both", padx=0, pady=0)

        title_label = ctk.CTkLabel(
            news_n_updates,
            fg_color=bg,
            bg_color=bg,
            image=icons["news_icon"],
            compound="top",
            text="News and Updates",
            text_color=text_fg,
            font=("Helvetica", -18, "bold")
        )
        title_label.pack(fill="x", pady=(30, 0))

        # News frame
        news_frame = ctk.CTkFrame(news_n_updates, fg_color=fg, corner_radius=0)
        news_frame.pack(fill="x", padx=30, pady=10)

        with open(news_txt_path, "rb") as f:
            lines = f.readlines()

        self.news_1 = lines[0].strip() if len(lines) > 0 else ""
        self.news_2 = lines[1].strip() if len(lines) > 1 else ""
        self.news_3 = lines[2].strip() if len(lines) > 2 else ""
        self.news_4 = lines[3].strip() if len(lines) > 3 else ""

        # news 1
        news_1_frame = ctk.CTkFrame(news_frame, fg_color=fg)
        news_1_frame.pack(fill="x", padx=0, pady=0)

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
            font=("Helvetica", -14)
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
            font=("Helvetica", -14)
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
            font=("Helvetica", -14)
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
            font=("Helvetica", -14)
        )
        news_4_text.pack(side="left", padx=10, pady=0, ipadx=5, ipady=5)

        shortcuts_pframe = ctk.CTkFrame(main_scrollable_frame, fg_color=bg)
        shortcuts_pframe.pack(fill="x", padx=0, pady=0)

        title_label = ctk.CTkLabel(
            shortcuts_pframe,
            fg_color=bg,
            image=icons["shortcuts_icon"],
            compound="top",
            text="Shortcuts",               
            text_color=text_fg,
            font=("Helvetica", -18, "bold")
        )
        title_label.pack(side="top", fill="x", pady=(30, 0))

        # Shortcuts Frame
        shortcuts_frame = ctk.CTkFrame(shortcuts_pframe, fg_color=fg)          
        shortcuts_frame.pack(fill="x", padx=30, pady=10)
        
        # Shortcut 1
        shortcut_1_frame = ctk.CTkFrame(shortcuts_frame, fg_color=fg)
        shortcut_1_frame.grid(row=0, column=0, padx=(10, 20), pady=10, sticky="nsew")

        shortcut_1_icon = ctk.CTkLabel(
            shortcut_1_frame, 
            text="", 
            image=icons["shortcut_1_icon"], 
            height=120, 
            width=120
        )
        shortcut_1_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        shortcut_1_text = ctk.CTkLabel(
            shortcut_1_frame,
            text="Papers",
            text_color=text_fg,
            font=("Helvetica", -18, "bold")
        )
        shortcut_1_text.grid(row=0, column=1, padx=10, pady=(10, 0))

        shortcut_1_sub_text = ctk.CTkLabel(
            shortcut_1_frame,
            text="Keep track of your past and\n model papers, read them, delete them\n and add more papers etc.",
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        shortcut_1_sub_text.grid(row=1, column=1, padx=10, pady=0)

        go_to_papers_button = ctk.CTkButton(
            shortcut_1_frame,
            text="Go to papers",
            fg_color=btn_active,
            hover_color=btn_hvr,
            width=50,
            height=10,
            command=self.show_papers
        )
        go_to_papers_button.grid(row=2, column=1, padx=10, ipadx=1, ipady=1, pady=(0, 10))

        # Shortcut 2
        shortcut_2_frame = ctk.CTkFrame(shortcuts_frame, fg_color=fg)
        shortcut_2_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

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
            font=("Helvetica", -18, "bold")
        )
        shortcut_2_text.grid(row=0, column=1, padx=10, pady=(10, 0))

        shortcut_2_sub_text = ctk.CTkLabel(
            shortcut_2_frame,
            text="Stay up to date with ongoing\n examination's datesheets. Teachers will be \nableto change, remove or add exams.",
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        shortcut_2_sub_text.grid(row=1, column=1, padx=10, pady=0)

        go_to_exams_button = ctk.CTkButton(
            shortcut_2_frame,
            text="Go to Exams",
            fg_color=btn_active,
            hover_color=btn_hvr,
            width=50,
            height=10,
            command=self.show_examinations
            )
        go_to_exams_button.grid(row=2, column=1, padx=10, ipady=1, ipadx=1, pady=(0, 10))

        # Shortcut 3
        shortcut_3_frame = ctk.CTkFrame(shortcuts_frame, fg_color=fg)
        shortcut_3_frame.grid(row=0, column=2, padx=30, pady=10, sticky="nsew")

        shortcut_3_icon = ctk.CTkLabel(shortcut_3_frame, text="", image=icons["shortcut_3_icon"], height=120, width=120)
        shortcut_3_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        shortcut_3_text = ctk.CTkLabel(
            shortcut_3_frame,
            text="Results",
            text_color=text_fg,
            font=("Helvetica", -18, "bold")
        )
        shortcut_3_text.grid(row=0, column=1, padx=10, pady=(10, 0))

        shortcut_3_sub_text = ctk.CTkLabel(
            shortcut_3_frame,
            text="See the results of recent\n examination. The teachers will be able\nto add and remove the results.",
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        shortcut_3_sub_text.grid(row=1, column=1, padx=10, pady=0)

        go_to_results_button = ctk.CTkButton(
            shortcut_3_frame,
            text="Go to Results",
            fg_color=btn_active,
            hover_color=btn_hvr,
            width=50,
            height=10,
            command=self.show_results
            )
        go_to_results_button.grid(row=2, column=1, padx=10, ipady=1, ipadx=1, pady=(0, 10))
        
        title_label = ctk.CTkLabel(
            shortcuts_pframe,
            fg_color=bg,
            image=icons["help_icon"],
            compound="top",
            text="Roles and Help",
            text_color=text_fg,
            font=("Helvetica", -18, "bold")
        )
        title_label.pack(fill="x", pady=(30, 0))

        # about us and Roles frame
        about_roles_and_help = ctk.CTkFrame(shortcuts_pframe, fg_color=fg)
        about_roles_and_help.pack(fill="x", padx=30, pady=10)

        # admin role
        role_1_frame = ctk.CTkFrame(about_roles_and_help, fg_color=fg)
        role_1_frame.grid(row=0, column=0, padx=10, pady=20, sticky="nsew")

        role_1_icon = ctk.CTkLabel(role_1_frame, text="", image=icons["role_1_icon"], height=120, width=120)
        role_1_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        role_1_text = ctk.CTkLabel(
            role_1_frame,
            text="Admins",
            text_color=text_fg,
            font=("Helvetica", -18, "bold")
        )
        role_1_text.grid(row=0, column=1, padx=8, pady=(10, 0))

        role_1_sub_text = ctk.CTkLabel(
            role_1_frame,
            text="This role is for the staff of the school.\n They will have access to all features, they\n will be able to add, edit or remove\n exams, results and papers.",
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        role_1_sub_text.grid(row=1, column=1, padx=8, pady=0)

        # student role
        role_2_frame = ctk.CTkFrame(about_roles_and_help, fg_color=fg)
        role_2_frame.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

        role_2_icon = ctk.CTkLabel(role_2_frame, text="", image=icons["role_2_icon"], height=120, width=120)
        role_2_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        role_2_text = ctk.CTkLabel(
            role_2_frame,
            text="Students",
            text_color=text_fg,
            font=("Helvetica", -18, "bold")
        )
        role_2_text.grid(row=0, column=1, padx=10, pady=(10, 0))

        role_2_sub_text = ctk.CTkLabel(
            role_2_frame,
            text="This is the role for students.\nThey will not be able to access any exclusive\n features but they will be able to see news,\n exam datesheets, results and papers.",
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        role_2_sub_text.grid(row=1, column=1, padx=10, pady=0)

        # support & feedback
        support_frame = ctk.CTkFrame(about_roles_and_help, fg_color=fg)
        support_frame.grid(row=0, column=2, padx=10, pady=20, sticky="nsew")

        about_us_icon = ctk.CTkLabel(support_frame, text="", image=icons["support_icon"], height=120, width=120)
        about_us_icon.grid(row=0, column=0,rowspan=3, padx=(10, 0), pady=10)

        help_text = ctk.CTkLabel(
            support_frame,
            text="Help & Feedback",
            text_color=text_fg,
            font=("Helvetica", -18, "bold")
        )
        help_text.grid(row=0, column=1, padx=10, pady=(10, 5))

        help_sub_text = ctk.CTkLabel(
            support_frame,
            text="Have you been in any kind of issue\n while using our program and want it to be\n fixed? Please let us know and we will try\n our best to fix it ASAP.",
            text_color=text_fg,
            font=("Helvetica", -14)
        )
        help_sub_text.grid(row=1, column=1, padx=10, ipadx=5, pady=5)

        # buttons frame
        buttons_frame = ctk.CTkFrame(main_scrollable_frame, fg_color=bg)
        buttons_frame.pack(side="bottom", fill="x", padx=30, pady=0, ipady=0)

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
                hover_color=btn_hvr,
                image=edit_button_icon,
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

    def show_students(self):
        self.clear_main_frame()
        self.set_button_state(self.student_button)

        main_frame = ctk.CTkFrame(
            self.main_frame, 
            fg_color=bg,
            border_width=2,
            border_color=btn_active,
            )
        main_frame.pack(expand="true", padx=5, pady=5)

        if self.role == "admin":
            # add button
            add_student_button = ctk.CTkButton(
                main_frame,
                text="Add Student",
                fg_color=bg,
                command=self.add_student_toplevel,
                text_color=text_fg,
                hover_color=fg,
                width=100,
                height=100,
                image=icons["add_icon"],
                compound="top",
                font=("helvetica", 18, "bold")
            )
            add_student_button.pack(side="left", padx=10, pady=10, ipadx=5, ipady=5)
            self.add_student_toplevel_window = None

            # get button
            get_button = ctk.CTkButton(
                main_frame,
                fg_color=bg,
                text="Get Students",
                command=self.get_student_toplevel,
                text_color=text_fg,
                width=100,
                height=100,
                hover_color=fg,
                image=icons["get_icon"],
                compound="top",
                font=("helvetica", 18, "bold")
            )
            get_button.pack(side="left", padx=10, pady=10, ipadx=5, ipady=5)
            self.get_student_toplevel_window = None

            # delete button
            delete_button = ctk.CTkButton(
                main_frame,
                fg_color=bg,
                text="Delete Student",
                command=self.del_student_toplevel,
                text_color=text_fg,
                hover_color=fg,
                width=100,
                height=100,
                image=icons["del_icon"],
                compound="top",
                font=("helvetica", 18, "bold")
            )
            delete_button.pack(side="left", padx=10, pady=10, ipadx=5, ipady=5)
            self.del_student_toplevel_window = None

        else:
            ctk.CTkLabel(
                main_frame, 
                fg_color=bg, 
                text_color=text_fg,
                text="You must be an administrator to add, get or remove any students from the database!",
                font=("helvetica", 18, "bold")
            ).pack(padx=50, pady=50)

    def show_examinations(self):
        
        # Clear the main frame and set the button state
        self.clear_main_frame()
        self.set_button_state(self.exams_button)

        # Create the scrollable frame
        scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color=bg,
            scrollbar_button_color=btn_active, 
            scrollbar_button_hover_color=btn_hvr, 
        )
        scrollable_frame.pack(fill="both", expand=True, side="top", pady=5, padx=5)

        # populate the scrollable frame with the datsheets
        datesheet.GetDatesheet(scrollable_frame)

        if self.role == "admin": 

            # Edit Exam Buttons frame
            edit_exam_btn_frame = ctk.CTkFrame(self.main_frame, fg_color=bg)
            edit_exam_btn_frame.pack(side="bottom", fill="x", padx=10, pady=5)

            # Add SSC-I Exam
            add_ssc_1_exam_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=add_exams_button_icon,
                text="Edit Exams",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr,
                command=self.manage_exams_toplevel,
                height=12,
                width=40,
            )
            add_ssc_1_exam_btn.grid(row=0, column=0,padx=5, pady=(0, 5), sticky="we")

            # Refresh button
            refresh_btn = ctk.CTkButton(
                edit_exam_btn_frame,
                image=refresh_pdfs_button_icon,
                text="Refresh",
                text_color=text_fg_2,
                fg_color=btn_active,
                hover_color=btn_hvr,
                command=self.show_examinations,
                height=12,
                width=40,
            )
            refresh_btn.grid(row=0, column=1, padx=5, pady=(0, 5), sticky="we")

            self.manage_exams_toplevel_window = None

    def show_results(self):
        # clears the main frame and sets the button state
        self.clear_main_frame()
        self.set_button_state(self.results_button)

        scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame, 
            fg_color=bg,
            scrollbar_button_color=btn_active, 
            scrollbar_button_hover_color=btn_hvr,   
        )
        scrollable_frame.pack(fill="both", expand="true", padx=5, pady=5)

        get_result_frame = ctk.CTkFrame(scrollable_frame, fg_color=bg)
        get_result_frame.pack(side="top", expand="true", fill="both", padx=10, pady=10)

        search_frame = ctk.CTkFrame(get_result_frame, fg_color=bg)
        search_frame.pack(side="top", padx=10, pady=10)

        result_frame = ctk.CTkFrame(get_result_frame, fg_color=bg)
        result_frame.pack(padx=10, pady=10, expand="true")

        search_entry = ctk.CTkEntry(search_frame, placeholder_text="Enter roll no...", width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        search_entry.pack(side="left", padx=5, pady=5)

        search_btn = ctk.CTkButton(
            search_frame,
            text="Search",
            fg_color=btn_active,
            command=lambda: get_results.GetResult(result_frame, search_entry),
            hover_color=btn_hvr
        )
        search_btn.pack(side="right", padx=5, pady=5)

        if self.role == "admin":
            btn_frame = ctk.CTkFrame(scrollable_frame, fg_color=bg)
            btn_frame.pack(side="bottom", padx=10, pady=10)

            btn1 = ctk.CTkButton(
                btn_frame,
                text="Add CS SSC",
                fg_color=btn_active,
                hover_color=btn_hvr,
                command=self.add2csssc_toplevel
            )
            btn1.pack(side="left", padx=5, pady=5)  
            self.add2csssc_toplevel_window = None

            btn2 = ctk.CTkButton(
                btn_frame,
                text="Add PM SSC",
                fg_color=btn_active,
                hover_color=btn_hvr,
                command=self.add2pmssc_toplevel
            )
            btn2.pack(side="left", padx=5, pady=5)
            self.add2pmssc_toplevel_window = None

            btn3 = ctk.CTkButton(
                btn_frame,
                text="Add CS HSSC",
                fg_color=btn_active,
                hover_color=btn_hvr,
                command=self.add2cshssc_toplevel
            )
            btn3.pack(side="left", padx=5, pady=5)
            self.add2cshssc_toplevel_window = None

            btn4 = ctk.CTkButton(
                btn_frame,
                text="Add PM HSSC",
                fg_color=btn_active,
                hover_color=btn_hvr,
                command=self.add2pmhssc_toplevel
            )
            btn4.pack(side="left", padx=5, pady=5)
            self.add2pmhssc_toplevel_window = None

    def show_papers(self):
        # Clear the main frame and set the button state
        self.clear_main_frame()
        self.set_button_state(self.papers_button)

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame, 
            fg_color=bg,
            scrollbar_button_color=btn_active, 
            scrollbar_button_hover_color=btn_hvr, 
        )
        self.scrollable_frame.pack(side="top", fill="both", padx=5, ipadx=0, pady=5, expand=True)

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
            height=12,
            width=40,
            hover_color=btn_hvr,
            command=self.refresh_pdfs
        )
        refresh_pdfs_button.pack(side="left", padx=5, ipadx=5, pady=5)

        # Add papers button
        add_paper_button = ctk.CTkButton(
            self.button_frame,
            text="Add Papers",
            text_color=text_fg_2,
            image=add_paper_button_icon,
            hover_color=btn_hvr,
            fg_color=btn_active,
            height=12,
            width=40,
            command=self.add_paper
        )
        add_paper_button.pack(side="left", padx=5, ipadx=5, pady=5)

        # Delete papers button
        delete_paper_button = ctk.CTkButton(
            self.button_frame,
            text="Remove Papers",
            text_color=text_fg_2,
            image=delete_paper_button_icon,
            hover_color=btn_hvr,
            height=12,
            width=40,
            fg_color=btn_active,
            command=self.delete_paper
        )
        delete_paper_button.pack(side="left", padx=5, ipadx=5, pady=5)

        # Search papers button
        search_paper_button = ctk.CTkButton(
            self.button_frame,
            text="",
            image=search_button_icon,
            hover_color=fg,
            height=12,
            width=12,  
            fg_color="transparent",
            command=self.search_paper
        )
        search_paper_button.pack(side="right", padx=(2, 10), pady=0)
        
        # Search entry
        self.search_entry = ctk.CTkEntry(
            self.button_frame, 
            placeholder_text="Search here...", 
            placeholder_text_color=text_fg, 
            width=200, 
            height=12,
            fg_color=fg,
            border_width=1,
            border_color=btn_active
        )
        self.search_entry.pack(side="right", padx=(5, 2), pady=5)

        # Load the pdfs to the main scrollable frame
        self.load_pdfs(default_pdfs_path)

# helper function for show home section
    def show_profile(self):
        if self.show_profile_toplevel_window is None or not self.show_profile_toplevel_window.winfo_exists():
            self.show_profile_toplevel_window = show_profile.CurrentAccount(self)
        else:
            self.show_profile_toplevel_window.focus()

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

# helper functions for show students section
    def add_student_toplevel(self):
        if self.add_student_toplevel_window is None or not self.add_student_toplevel_window.winfo_exists():
            self.add_student_toplevel_window = show_student.AddStudent(self)
        else:
            self.add_student_toplevel_window.focus()

    def get_student_toplevel(self):
        if self.get_student_toplevel_window is None or not self.get_student_toplevel_window.winfo_exists():
            self.get_student_toplevel_window = show_student.GetStudent(self)
        else:
            self.get_student_toplevel_window.focus()

    def del_student_toplevel(self):
        if self.del_student_toplevel_window is None or not self.del_student_toplevel_window.winfo_exists():
            self.del_student_toplevel_window = show_student.DeleteStudent(self)
        else:
            self.del_student_toplevel_window.focus()

# helper function for show examination section
    def manage_exams_toplevel(self):
        if self.manage_exams_toplevel_window is None or not self.manage_exams_toplevel_window.winfo_exists():
            self.manage_exams_toplevel_window = manage_exams.ManageExams(self)
        else:
            self.manage_exams_toplevel_window.focus()

# helper function for show results section
    def add2csssc_toplevel(self):
        if self.add2csssc_toplevel_window is None or not self.add2csssc_toplevel_window.winfo_exists():
            self.add2csssc_toplevel_window = show_results.AddResult2CSSSC(self)
        else:
            self.add2csssc_toplevel_window.focus()

    def add2pmssc_toplevel(self):
        if self.add2pmssc_toplevel_window is None or not self.add2pmssc_toplevel_window.winfo_exists():
            self.add2pmssc_toplevel_window = show_results.AddResult2PMSSC(self)
        else:
            self.add2pmssc_toplevel_window.focus()

    def add2cshssc_toplevel(self):
        if self.add2cshssc_toplevel_window is None or not self.add2cshssc_toplevel_window.winfo_exists():
            self.add2cshssc_toplevel_window = show_results.AddResult2CSHSSC(self)
        else:
            self.add2cshssc_toplevel_window.focus()

    def add2pmhssc_toplevel(self):
        if self.add2pmhssc_toplevel_window is None or not self.add2pmhssc_toplevel_window.winfo_exists():
            self.add2pmhssc_toplevel_window = show_results.AddResult2PMHSSC(self)
        else:
            self.add2pmhssc_toplevel_window.focus()

# helper functions for show papers section
    def search_paper(self):
        query = self.search_entry.get().strip()
        if query:
            # Clear the current content in the scrollable frame
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            # Search through the PDF files in the directory
            pdf_files = [f for f in os.listdir(default_pdfs_path) if f.endswith('.pdf')]

            matching_files = [f for f in pdf_files if query in f.lower()]

            if matching_files:
                row, col = 0, 0
                max_columns = 8
                for pdf_file in matching_files:
                    pdf_path = os.path.join(default_pdfs_path, pdf_file)
                    self.add_pdf_tile(self.scrollable_frame, pdf_path, row, col)
                    col += 1
                    if col >= max_columns:
                        col = 0
                        row += 1
            else:
                messagebox.showinfo("No Results", "No matching papers found.")
        else:
            messagebox.showerror("Error", "Please enter a search query.")
        
    def refresh_pdfs(self):
        self.load_pdfs(default_pdfs_path)
    
    def add_paper(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            dest_path = os.path.join(default_pdfs_path, os.path.basename(pdf_path))
            if not os.path.exists(dest_path):
                shutil.copy(pdf_path, dest_path)

    def delete_paper(self):
        pdf_path = filedialog.askopenfilename(initialdir=default_pdfs_path, filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            os.remove(pdf_path)

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

            tile_frame = ctk.CTkFrame(frame, width=width, height=250, fg_color=bg)
            tile_frame.grid(row=row, column=col, padx=7, pady=10, ipadx=0, ipady=0)
            tile_frame.grid_propagate(False)

            file_name = os.path.basename(pdf_path)
            if len(file_name) > 15:
                file_name = file_name[:15] + "..."

            tile_button = ctk.CTkButton(
                tile_frame,
                text=file_name,
                image=img_tk,                   
                compound="top",
                text_color=text_fg,
                hover_color=btn_hvr,
                fg_color=fg,
                command=lambda path=pdf_path: self.open_pdf(path)
            )
            tile_button.pack(fill="both", side="top", padx=0, pady=0, ipadx=7, ipady=15)

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
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

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
