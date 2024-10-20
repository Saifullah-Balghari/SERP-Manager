import customtkinter as ctk
from  PIL import Image, ImageTk

from ...helpers.settings import *
from ...helpers import database as db
from ...helpers import messagebox

# Color scheme
bg = "#FCFAFF"
fg = "#F4EBFF"
text_fg_2 = "#FFFFFF"   
btn_hvr = "#7F56D9"
btn_active = "#6941C6"
text_fg = "#53389E"


class AddResult2CSSSC(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("TopLevel - Add Results - CS - SSC")
        self.geometry("1200x600")
        self.configure(fg_color=bg)
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.update()
        self.grab_set()

        self.widget()
    
    def widget(self):
        add_icon = ImageTk.PhotoImage(Image.open(add_exams_icon_path).resize((60, 60)), Image.LANCZOS) 

        title_label = ctk.CTkLabel(
            self,
            image=add_icon,
            compound="top",
            text="Add Results",
            font=("helvetica", -18, "bold"),
            text_color=text_fg
        )
        title_label.pack(fill="x", side="top", pady=(10, 0))

        sub_title_label = ctk.CTkLabel(
            self,
            text="Enter the details below, submit and wait for the confirmation message",
            font=("Helvetica", -14),
            text_color="grey"
        )
        sub_title_label.pack(side="top", fill="x",pady=(0, 5))

        main_frame = ctk.CTkFrame(master=self, fg_color=bg, border_width=2, border_color=btn_active)
        main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        result_form_frame = ctk.CTkFrame(main_frame, fg_color=bg)
        result_form_frame.pack(padx=30, pady=10, ipadx=20)

        # roll number input
        roll_label = ctk.CTkLabel(result_form_frame, text="Roll Number:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        roll_label.grid(row=0, column=0, padx=5, pady=10)
        self.roll_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.roll_entry.grid(row=0, column=1, padx=5, pady=10)        

        # exam name name input
        name_label = ctk.CTkLabel(result_form_frame, text="Examination:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        name_label.grid(row=1, column=0, padx=5, pady=10)
        self.name_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.name_entry.grid(row=1, column=1, padx=5, pady=10)        

        # math name input
        s1_label = ctk.CTkLabel(result_form_frame, text="Mathematics:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s1_label.grid(row=2, column=0, padx=5, pady=10)
        self.s1_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s1_entry.grid(row=2, column=1, padx=5, pady=10)      

        # phy name input
        s2_label = ctk.CTkLabel(result_form_frame, text="Physics:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s2_label.grid(row=3, column=0, padx=5, pady=10)
        self.s2_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s2_entry.grid(row=3, column=1, padx=5, pady=10)

        # chem input
        s3_label = ctk.CTkLabel(result_form_frame, text="Chemistry:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s3_label.grid(row=4, column=0, padx=5, pady=10)
        self.s3_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s3_entry.grid(row=4, column=1, padx=5, pady=10)

        # cs input
        s4_label = ctk.CTkLabel(result_form_frame, text="Computer Science:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s4_label.grid(row=0, column=2, padx=(65, 5), pady=10)
        self.s4_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s4_entry.grid(row=0, column=3, padx=5, pady=10)

        # ps number input
        s5_label = ctk.CTkLabel(result_form_frame, text="Pak-Studies:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s5_label.grid(row=1, column=2, padx=(65, 5), pady=10)
        self.s5_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s5_entry.grid(row=1, column=3, padx=5, pady=10)
        
        # isl adddress imput
        s6_label = ctk.CTkLabel(result_form_frame, text="Islamiyat:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s6_label.grid(row=2, column=2, padx=(65, 5), pady=10)
        self.s6_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s6_entry.grid(row=2, column=3, padx=5, pady=10)

        # urdu address input
        s7_label = ctk.CTkLabel(result_form_frame, text="Urdu:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s7_label.grid(row=3, column=2, padx=(65, 5), pady=10)
        self.s7_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s7_entry.grid(row=3, column=3, padx=5, pady=10)

        # eng address input
        s8_label = ctk.CTkLabel(result_form_frame, text="English:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s8_label.grid(row=4, column=2, padx=(65, 5), pady=10)
        self.s8_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s8_entry.grid(row=4, column=3, padx=5, pady=10)

        # submit button
        submit_button = ctk.CTkButton(
            main_frame,
            text="Submit",
            command=self.add_result,
            text_color=text_fg_2,
            hover_color=btn_hvr,
            fg_color=btn_active
        )
        submit_button.pack(padx=10, pady=10)

    def add_result(self):
        roll_no = self.roll_entry.get()
        exam_name = self.name_entry.get()
        math = self.s1_entry.get()
        physics = self.s2_entry.get()
        chemistry = self.s3_entry.get()
        computer = self.s4_entry.get()
        pak_studies = self.s5_entry.get()
        islamiyat = self.s6_entry.get()
        urdu = self.s7_entry.get()
        english = self.s8_entry.get()
        total_marks = 550

        if not roll_no or not exam_name or not math or not physics or not chemistry or not computer or not pak_studies or not islamiyat or not urdu or not english:
            messagebox.show_error("Error", "All fields are required!")
            return

        if (not (0 <= int(math) <= 75) or not (0 <= int(physics) <= 75) or not (0 <= int(chemistry) <= 75)or not (0 <= int(computer) <= 75)
             or not (0 <= int(pak_studies) <= 50)or not (0 <= int(islamiyat) <= 50) or not (0 <= int(urdu) <= 75) or not (0 <= int(english) <= 75)):
            messagebox.show_error("Error", "Marks should be between 0 and 75")
            return

        if db.student_exist(roll_no):
            if db.add_result_2_cs_ssc(roll_no, exam_name, math, physics, chemistry, computer, pak_studies, islamiyat, urdu, english, total_marks):
                messagebox.show_info("Success", "Result added successfully!")
                self.roll_entry.delete(0, "end")
                self.name_entry.delete(0, "end")
                self.s1_entry.delete(0, "end")
                self.s2_entry.delete(0, "end")
                self.s3_entry.delete(0, "end")
                self.s4_entry.delete(0, "end")
                self.s5_entry.delete(0, "end")
                self.s6_entry.delete(0, "end")
                self.s7_entry.delete(0, "end")
                self.s8_entry.delete(0, "end")
                return
            else:
                messagebox.show_error("Error", "Failed to add result!")
        else:
            messagebox.show_error("Error", "Student not found!")


class AddResult2PMSSC(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("TopLevel - Add Results - PM - SSC")
        self.geometry("1200x600")
        self.configure(fg_color=bg)
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.update()
        self.grab_set()

        self.widget()
    
    def widget(self):
        add_icon = ImageTk.PhotoImage(Image.open(add_exams_icon_path).resize((60, 60)), Image.LANCZOS) 

        title_label = ctk.CTkLabel(
            self,
            image=add_icon,
            compound="top",
            text="Add Results",
            font=("helvetica", -18, "bold"),
            text_color=text_fg
        )
        title_label.pack(fill="x", side="top", pady=(10, 0))

        sub_title_label = ctk.CTkLabel(
            self,
            text="Enter the details below, submit and wait for the confirmation message",
            font=("Helvetica", -14),
            text_color="grey"
        )
        sub_title_label.pack(side="top", fill="x",pady=(0, 5))

        main_frame = ctk.CTkFrame(master=self, fg_color=bg, border_width=2, border_color=btn_active)
        main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        result_form_frame = ctk.CTkFrame(main_frame, fg_color=bg)
        result_form_frame.pack(padx=30, pady=10, ipadx=20)

        # roll number input
        roll_label = ctk.CTkLabel(result_form_frame, text="Roll Number:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        roll_label.grid(row=0, column=0, padx=5, pady=10)
        self.roll_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.roll_entry.grid(row=0, column=1, padx=5, pady=10)        

        # exam name name input
        name_label = ctk.CTkLabel(result_form_frame, text="Examination:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        name_label.grid(row=1, column=0, padx=5, pady=10)
        self.name_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.name_entry.grid(row=1, column=1, padx=5, pady=10)        

        # math name input
        s1_label = ctk.CTkLabel(result_form_frame, text="Mathematics:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s1_label.grid(row=2, column=0, padx=5, pady=10)
        self.s1_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s1_entry.grid(row=2, column=1, padx=5, pady=10)      

        # phy name input
        s2_label = ctk.CTkLabel(result_form_frame, text="Physics:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s2_label.grid(row=3, column=0, padx=5, pady=10)
        self.s2_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s2_entry.grid(row=3, column=1, padx=5, pady=10)

        # chem input
        s3_label = ctk.CTkLabel(result_form_frame, text="Chemistry:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s3_label.grid(row=4, column=0, padx=5, pady=10)
        self.s3_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s3_entry.grid(row=4, column=1, padx=5, pady=10)

        # cs input
        s4_label = ctk.CTkLabel(result_form_frame, text="Biology:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s4_label.grid(row=0, column=2, padx=(65, 5), pady=10)
        self.s4_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s4_entry.grid(row=0, column=3, padx=5, pady=10)

        # ps number input
        s5_label = ctk.CTkLabel(result_form_frame, text="Pak-Studies:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s5_label.grid(row=1, column=2, padx=(65, 5), pady=10)
        self.s5_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s5_entry.grid(row=1, column=3, padx=5, pady=10)
        
        # isl adddress imput
        s6_label = ctk.CTkLabel(result_form_frame, text="Islamiyat:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s6_label.grid(row=2, column=2, padx=(65, 5), pady=10)
        self.s6_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s6_entry.grid(row=2, column=3, padx=5, pady=10)

        # urdu address input
        s7_label = ctk.CTkLabel(result_form_frame, text="Urdu:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s7_label.grid(row=3, column=2, padx=(65, 5), pady=10)
        self.s7_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s7_entry.grid(row=3, column=3, padx=5, pady=10)

        # eng address input
        s8_label = ctk.CTkLabel(result_form_frame, text="English:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s8_label.grid(row=4, column=2, padx=(65, 5), pady=10)
        self.s8_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s8_entry.grid(row=4, column=3, padx=5, pady=10)

        # submit button
        submit_button = ctk.CTkButton(
            main_frame,
            text="Submit",
            command=self.add_result,
            text_color=text_fg_2,
            hover_color=btn_hvr,
            fg_color=btn_active
        )
        submit_button.pack(padx=10, pady=10)

    def add_result(self):
        roll_no = self.roll_entry.get()
        exam_name = self.name_entry.get()
        math = self.s1_entry.get()
        physics = self.s2_entry.get()
        chemistry = self.s3_entry.get()
        biology = self.s4_entry.get()
        pak_studies = self.s5_entry.get()
        islamiyat = self.s6_entry.get()
        urdu = self.s7_entry.get()
        english = self.s8_entry.get()
        total_marks = 550

        if not roll_no or not exam_name or not math or not physics or not chemistry or not biology or not pak_studies or not islamiyat or not urdu or not english:
            messagebox.show_error("Error", "All fields are required!")
            return

        if (not (0 <= int(math) <= 75) or not (0 <= int(physics) <= 75) or not (0 <= int(chemistry) <= 75)or not (0 <= int(biology) <= 75)
             or not (0 <= int(pak_studies) <= 50)or not (0 <= int(islamiyat) <= 50) or not (0 <= int(urdu) <= 75) or not (0 <= int(english) <= 75)):
            messagebox.show_error("Error", "Marks should be between 0 and 75")
            return

        if db.student_exist(roll_no):
            if db.add_result_2_pm_ssc(roll_no, exam_name, math, physics, chemistry, biology, pak_studies, islamiyat, urdu, english, total_marks):
                messagebox.show_info("Success", "Result added successfully!")
                self.roll_entry.delete(0, "end")
                self.name_entry.delete(0, "end")
                self.s1_entry.delete(0, "end")
                self.s2_entry.delete(0, "end")
                self.s3_entry.delete(0, "end")
                self.s4_entry.delete(0, "end")
                self.s5_entry.delete(0, "end")
                self.s6_entry.delete(0, "end")
                self.s7_entry.delete(0, "end")
                self.s8_entry.delete(0, "end")
            else:
                messagebox.show_error("Error", "Failed to add result!")
        else:
            messagebox.show_error("Error", "Student not found!")


class AddResult2CSHSSC(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("TopLevel - Add Results - CS - HSSC")
        self.geometry("1200x600")
        self.configure(fg_color=bg)
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.update()
        self.grab_set()

        self.widget()
    
    def widget(self):
        add_icon = ImageTk.PhotoImage(Image.open(add_exams_icon_path).resize((60, 60)), Image.LANCZOS) 

        title_label = ctk.CTkLabel(
            self,
            image=add_icon,
            compound="top",
            text="Add Results",
            font=("helvetica", -18, "bold"),
            text_color=text_fg
        )
        title_label.pack(fill="x", side="top", pady=(10, 0))

        sub_title_label = ctk.CTkLabel(
            self,
            text="Enter the details below, submit and wait for the confirmation message",
            font=("Helvetica", -14),
            text_color="grey"
        )
        sub_title_label.pack(side="top", fill="x",pady=(0, 5))

        main_frame = ctk.CTkFrame(master=self, fg_color=bg, border_width=2, border_color=btn_active)
        main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        result_form_frame = ctk.CTkFrame(main_frame, fg_color=bg)
        result_form_frame.pack(padx=30, pady=10, ipadx=20)

        # roll number input
        roll_label = ctk.CTkLabel(result_form_frame, text="Roll Number:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        roll_label.grid(row=0, column=0, padx=5, pady=10)
        self.roll_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.roll_entry.grid(row=0, column=1, padx=5, pady=10)        

        # exam name name input
        name_label = ctk.CTkLabel(result_form_frame, text="Examination:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        name_label.grid(row=1, column=0, padx=5, pady=10)
        self.name_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.name_entry.grid(row=1, column=1, padx=5, pady=10)        

        # math name input
        s1_label = ctk.CTkLabel(result_form_frame, text="Mathematics:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s1_label.grid(row=2, column=0, padx=5, pady=10)
        self.s1_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s1_entry.grid(row=2, column=1, padx=5, pady=10)      

        # phy name input
        s2_label = ctk.CTkLabel(result_form_frame, text="Physics:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s2_label.grid(row=3, column=0, padx=5, pady=10)
        self.s2_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s2_entry.grid(row=3, column=1, padx=5, pady=10)

        # cs number input200
        s3_label = ctk.CTkLabel(result_form_frame, text="Computer Science:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s3_label.grid(row=0, column=2, padx=(65, 5), pady=10)
        self.s3_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s3_entry.grid(row=0, column=3, padx=5, pady=10)
        
        # isl/ps adddress imput
        s4_label = ctk.CTkLabel(result_form_frame, text="Islamiyat/Pak-Studies:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s4_label.grid(row=1, column=2, padx=(65, 5), pady=10)
        self.s4_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s4_entry.grid(row=1, column=3, padx=5, pady=10)

        # urdu address input
        s5_label = ctk.CTkLabel(result_form_frame, text="Urdu:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s5_label.grid(row=2, column=2, padx=(65, 5), pady=10)
        self.s5_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s5_entry.grid(row=2, column=3, padx=5, pady=10)

        # eng address input
        s6_label = ctk.CTkLabel(result_form_frame, text="English:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s6_label.grid(row=3, column=2, padx=(65, 5), pady=10)
        self.s6_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s6_entry.grid(row=3, column=3, padx=5, pady=10)

        # submit button
        submit_button = ctk.CTkButton(
            main_frame,
            text="Submit",
            command=self.add_result,
            text_color=text_fg_2,
            hover_color=btn_hvr,
            fg_color=btn_active
        )
        submit_button.pack(padx=10, pady=10)

    def add_result(self):
        roll_no = self.roll_entry.get()
        exam_name = self.name_entry.get()
        math = self.s1_entry.get()
        physics = self.s2_entry.get()
        computer = self.s3_entry.get()
        islamiyat_pak_studies = self.s4_entry.get()
        urdu = self.s5_entry.get()
        english = self.s6_entry.get()
        total_marks = 550

        if not roll_no.isdigit() or not exam_name or not math or not physics or not computer or not islamiyat_pak_studies or not urdu or not english:
            messagebox.show_error("Error", "All fields are required!")
            return
        
        if not (0 <= int(math) <= 100) or not (0 <= int(physics) <= 100) or not (0 <= int(computer) <= 100) or not (0 <= int(urdu) <= 100) or not (0 <= int(english) <= 100) or not (0 <= int(islamiyat_pak_studies) <= 50):
            messagebox.show_error("Error", "Marks should be between 0 and 100")
            return

        if db.student_exist(roll_no):
            if db.add_result_2_cs_hssc(roll_no, exam_name, math, physics, computer, islamiyat_pak_studies, urdu, english, total_marks):
                messagebox.show_info("Success", "Result added successfully!")
                self.roll_entry.delete(0, "end")
                self.name_entry.delete(0, "end")
                self.s1_entry.delete(0, "end")
                self.s2_entry.delete(0, "end")
                self.s3_entry.delete(0, "end")
                self.s4_entry.delete(0, "end")
                self.s5_entry.delete(0, "end")
                self.s6_entry.delete(0, "end")
            else:
                messagebox.show_error("Error", "Failed to add result!")
        else:
            messagebox.show_error("Error", "Student not found!")



class AddResult2PMHSSC(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("TopLevel - Add Results - PM - HSSC")
        self.geometry("1200x600")
        self.configure(fg_color=bg)
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.update()
        self.grab_set()

        self.widget()
    
    def widget(self):
        add_icon = ImageTk.PhotoImage(Image.open(add_exams_icon_path).resize((60, 60)), Image.LANCZOS) 

        title_label = ctk.CTkLabel(
            self,
            image=add_icon,
            compound="top",
            text="Add Results",
            font=("helvetica", -18, "bold"),
            text_color=text_fg
        )
        title_label.pack(fill="x", side="top", pady=(10, 0))

        sub_title_label = ctk.CTkLabel(
            self,
            text="Enter the details below, submit and wait for the confirmation message",
            font=("Helvetica", -14),
            text_color="grey"
        )
        sub_title_label.pack(side="top", fill="x",pady=(0, 5))

        main_frame = ctk.CTkFrame(master=self, fg_color=bg, border_width=2, border_color=btn_active)
        main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        result_form_frame = ctk.CTkFrame(main_frame, fg_color=bg)
        result_form_frame.pack(padx=30, pady=10, ipadx=20)

        # roll number input
        roll_label = ctk.CTkLabel(result_form_frame, text="Roll Number:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        roll_label.grid(row=0, column=0, padx=5, pady=10)
        self.roll_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.roll_entry.grid(row=0, column=1, padx=5, pady=10)        

        # exam name name input
        name_label = ctk.CTkLabel(result_form_frame, text="Examination:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        name_label.grid(row=1, column=0, padx=5, pady=10)
        self.name_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.name_entry.grid(row=1, column=1, padx=5, pady=10)        

        # math name input
        s1_label = ctk.CTkLabel(result_form_frame, text="Chemistry:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s1_label.grid(row=2, column=0, padx=5, pady=10)
        self.s1_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s1_entry.grid(row=2, column=1, padx=5, pady=10)      

        # phy name input
        s2_label = ctk.CTkLabel(result_form_frame, text="Physics:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s2_label.grid(row=3, column=0, padx=5, pady=10)
        self.s2_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s2_entry.grid(row=3, column=1, padx=5, pady=10)

        # cs number input
        s3_label = ctk.CTkLabel(result_form_frame, text="Biology:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s3_label.grid(row=0, column=2, padx=(65, 5), pady=10)
        self.s3_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s3_entry.grid(row=0, column=3, padx=5, pady=10)
        
        # isl/ps adddress imput
        s4_label = ctk.CTkLabel(result_form_frame, text="Islamiyat/Pak-Studies:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s4_label.grid(row=1, column=2, padx=(65, 5), pady=10)
        self.s4_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s4_entry.grid(row=1, column=3, padx=5, pady=10)

        # urdu address input
        s5_label = ctk.CTkLabel(result_form_frame, text="Urdu:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s5_label.grid(row=2, column=2, padx=(65, 5), pady=10)
        self.s5_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s5_entry.grid(row=2, column=3, padx=5, pady=10)

        # eng address input
        s6_label = ctk.CTkLabel(result_form_frame, text="English:", font=("Helvetica", -18, "bold"), text_color=text_fg)
        s6_label.grid(row=3, column=2, padx=(65, 5), pady=10)
        self.s6_entry = ctk.CTkEntry(result_form_frame, width=200, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.s6_entry.grid(row=3, column=3, padx=5, pady=10)

        # submit button
        submit_button = ctk.CTkButton(
            main_frame,
            text="Submit",
            command=self.add_result,
            text_color=text_fg_2,
            hover_color=btn_hvr,
            fg_color=btn_active
        )
        submit_button.pack(padx=10, pady=10)

    def add_result(self):
        roll_no = self.roll_entry.get()
        exam_name = self.name_entry.get()
        chemistry = self.s1_entry.get()
        physics = self.s2_entry.get()
        biology = self.s3_entry.get()
        islamiyat_pak_studies = self.s4_entry.get()
        urdu = self.s5_entry.get()
        english = self.s6_entry.get()
        total_marks = 550

        if not roll_no.isdigit() or not exam_name or not chemistry or not physics or not biology or not islamiyat_pak_studies or not urdu or not english:
            messagebox.show_error("Error", "All fields are required!")
            return
        
        if not (0 <= int(chemistry) <= 100) or not (0 <= int(physics) <= 100) or not (0 <= int(biology) <= 100) or not (0 <= int(urdu) <= 100) or not (0 <= int(english) <= 100) or not (0 <= int(islamiyat_pak_studies) <= 50):
            messagebox.show_error("Error", "Marks should be between 0 and 100")
            return

        if db.student_exist(roll_no):
            if db.add_result_2_pm_hssc(roll_no, exam_name, physics, chemistry, biology, islamiyat_pak_studies, urdu, english, total_marks):
                messagebox.show_info("Success", "Result added successfully!")
                self.roll_entry.delete(0, "end")
                self.name_entry.delete(0, "end")
                self.s1_entry.delete(0, "end")
                self.s2_entry.delete(0, "end")
                self.s3_entry.delete(0, "end")  
                self.s4_entry.delete(0, "end")
                self.s5_entry.delete(0, "end")
                self.s6_entry.delete(0, "end")
            else:
                messagebox.show_error("Error", "Failed to add result!")
        else:
            messagebox.show_error("Error", "Student not found!")