import customtkinter as ctk

from ...settings import *
from ... import messagebox

import json

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"   
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"

class GetDatesheet():
    def __init__(self, scrollable_frame):

        self.widget(scrollable_frame)

        # Loads subject's icons respectively
        self.subject_icon_map = {
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

        ssc1_subjects = self.load_subjects(ssc1_json_path)
        ssc2_subjects = self.load_subjects(ssc2_json_path)
        hssc1_subjects = self.load_subjects(hssc1_json_path)
        hssc2_subjects = self.load_subjects(hssc2_json_path)


        if not ssc1_subjects:
            ssc1_label = ctk.CTkLabel(self.ssc_1_content_frame, text="No ongoing exams", font=("Helvetica", 18), text_color=text_fg)
            ssc1_label.pack(pady=50)
        else:
            for subject in ssc1_subjects:
                self.create_subject_frame(self.ssc_1_content_frame, subject)

        if not ssc2_subjects:
            ssc2_label = ctk.CTkLabel(self.ssc_2_content_frame, text="No ongoing exams", font=("Helvetica", 18), text_color=text_fg)
            ssc2_label.pack(pady=50)
        else:
            for subject in ssc2_subjects:
                self.create_subject_frame(self.ssc_2_content_frame, subject)

        if not hssc1_subjects:
            hssc1_label = ctk.CTkLabel(self.hssc_1_content_frame, text="No ongoing exams", font=("Helvetica", 18), text_color=text_fg)
            hssc1_label.pack(pady=50)
        else:
            for subject in hssc1_subjects:
                self.create_subject_frame(self.hssc_1_content_frame, subject)

        if not hssc2_subjects:
            hssc2_label = ctk.CTkLabel(self.hssc_2_content_frame, text="No ongoing exams", font=("Helvetica", 18), text_color=text_fg)
            hssc2_label.pack(pady=50)
        else:
            for subject in hssc2_subjects:
                self.create_subject_frame(self.hssc_2_content_frame, subject)

    def widget(self, scrollable_frame):
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
        self.ssc_1_content_frame = ctk.CTkScrollableFrame(
            ssc_1_frame, 
            fg_color=bg, 
            orientation="horizontal",
            scrollbar_button_color=fg, 
            scrollbar_button_hover_color=btn_hvr 
        )
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
        self.ssc_2_content_frame = ctk.CTkScrollableFrame(
            ssc_2_frame, 
            fg_color=bg, 
            orientation="horizontal",
            scrollbar_button_color=fg, 
            scrollbar_button_hover_color=btn_hvr
        )
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
        self.hssc_1_content_frame = ctk.CTkScrollableFrame(
            hssc_1_frame, 
            fg_color=bg, 
            orientation="horizontal",
            scrollbar_button_color=fg, 
            scrollbar_button_hover_color=btn_hvr
        )
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
        self.hssc_2_content_frame = ctk.CTkScrollableFrame(
            hssc_2_frame, 
            fg_color=bg, 
            orientation="horizontal",
            scrollbar_button_color=fg, 
            scrollbar_button_hover_color=btn_hvr
        )
        self.hssc_2_content_frame.pack(fill="x", padx=0, pady=0, ipady=0)

    def load_subjects(self, file_path):
            try:    
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    return data.get("subjects", [])
            except json.JSONDecodeError:
                messagebox.show_error("Error", f"The file {file_path} is not a valid JSON file or is empty.")
                return []
            except FileNotFoundError:
                print(f"Error: The file {file_path} was not found.")
                messagebox.show_error("Error", f"The file {file_path} was not found.")
                return []

    def create_subject_frame(self, parent_frame, subject_data):
        subject_name = subject_data["subject_name"]

        icon = self.subject_icon_map.get(subject_name, icons.get("default_icon"))

        sub_frame = ctk.CTkFrame(parent_frame, fg_color=fg)         
        sub_frame.pack(side="left", padx=5, pady=0, ipadx=5, ipady=2)

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
            text=f"Date:  {subject_data['date']}\nDay:  {subject_data['day']}\nTime:  {subject_data['time']}\nExam:  {subject_data['Exam']}",
            text_color=text_fg,
            font=("Helvetica", 12)
        )
        sub_sub_text.grid(row=1, column=1, padx=5, ipadx=2, pady=(0, 5))