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


class AddStudent(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("TopLevel - Add Student")
        self.geometry("1200x500")
        self.configure(fg_color=bg)
        self.resizable(False, False)

        self.widget()
    
    def widget(self):
        add_icon = ImageTk.PhotoImage(Image.open(add_exams_icon_path).resize((60, 60)), Image.LANCZOS) 

        title_label = ctk.CTkLabel(
            self,
            image=add_icon,
            compound="top",
            text="Add Student",
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


        student_form_frame = ctk.CTkFrame(main_frame, fg_color=bg)
        student_form_frame.pack(padx=30, pady=10, ipadx=20)

        # roll number input
        roll_label = ctk.CTkLabel(student_form_frame, text="Roll Number:", font=("Helvetica", 14), text_color=text_fg)
        roll_label.grid(row=0, column=0, padx=5, pady=10)
        self.roll_entry = ctk.CTkEntry(student_form_frame, width=400, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.roll_entry.grid(row=0, column=1, padx=5, pady=10)        

        # student name input
        name_label = ctk.CTkLabel(student_form_frame, text="Name:", font=("Helvetica", 13), text_color=text_fg)
        name_label.grid(row=1, column=0, padx=5, pady=10)
        self.name_entry = ctk.CTkEntry(student_form_frame, width=400, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.name_entry.grid(row=1, column=1, padx=5, pady=10)        

        # father name input
        father_label = ctk.CTkLabel(student_form_frame, text="Father's Name:", font=("Helvetica", 14), text_color=text_fg)
        father_label.grid(row=2, column=0, padx=5, pady=10)
        self.father_entry = ctk.CTkEntry(student_form_frame, width=400, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.father_entry.grid(row=2, column=1, padx=5, pady=10)      

        # institution name input
        institution_label = ctk.CTkLabel(student_form_frame, text="Institution:", font=("Helvetica", 14), text_color=text_fg)
        institution_label.grid(row=3, column=0, padx=5, pady=10)
        self.institution_entry = ctk.CTkEntry(student_form_frame, width=400, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.institution_entry.grid(row=3, column=1, padx=5, pady=10)

        # level input
        level_label = ctk.CTkLabel(student_form_frame, text="Level:", font=("Helvetica", 14), text_color=text_fg)
        level_label.grid(row=4, column=0, padx=5, pady=10)
        self.level_entry = ctk.CTkEntry(student_form_frame, placeholder_text="SSC or HSSC", width=400, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.level_entry.grid(row=4, column=1, padx=5, pady=10)

        # year input
        year_label = ctk.CTkLabel(student_form_frame, text="Year:", font=("Helvetica", 14), text_color=text_fg)
        year_label.grid(row=0, column=2, padx=(65, 5), pady=10)
        self.year_entry = ctk.CTkEntry(student_form_frame, placeholder_text="1st or 2nd", width=400, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.year_entry.grid(row=0, column=3, padx=5, pady=10)

        # contact number input
        contact_label = ctk.CTkLabel(student_form_frame, text="Contact Number:", font=("Helvetica", 14), text_color=text_fg)
        contact_label.grid(row=1, column=2, padx=(65, 5), pady=10)
        self.contact_entry = ctk.CTkEntry(student_form_frame, placeholder_text="+92XXXXXXXXXX", width=400, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.contact_entry.grid(row=1, column=3, padx=5, pady=10)
        
        # email adddress imput
        email_label = ctk.CTkLabel(student_form_frame, text="Email Address:", font=("Helvetica", 14), text_color=text_fg)
        email_label.grid(row=2, column=2, padx=(65, 5), pady=10)
        self.email_entry = ctk.CTkEntry(student_form_frame, placeholder_text="abc@xyz.com", width=400, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.email_entry.grid(row=2, column=3, padx=5, pady=10)

        # physical address input
        address_label = ctk.CTkLabel(student_form_frame, text="Physical Address:", font=("Helvetica", 14), text_color=text_fg)
        address_label.grid(row=3, column=2, padx=(65, 5), pady=10)
        self.address_entry = ctk.CTkEntry(student_form_frame, width=400, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.address_entry.grid(row=3, column=3, padx=5, pady=10)

        # submit button
        submit_button = ctk.CTkButton(
            main_frame,
            text="Submit",
            command=self.submit_student,
            text_color=text_fg_2,
            hover_color=btn_hvr,
            fg_color=btn_active
        )
        submit_button.pack(padx=10, pady=10)

    def submit_student(self):
        roll_no = self.roll_entry.get()
        student_name = self.name_entry.get()
        std_father_name = self.father_entry.get()
        institution = self.institution_entry.get()
        level = self.level_entry.get()
        year = self.year_entry.get()
        contact_no = self.contact_entry.get()
        mail = self.email_entry.get()
        address = self.address_entry.get()

        if not roll_no or not student_name or not std_father_name or not institution or not level or not year or not contact_no or not mail or not address:
            messagebox.showerror("Error", "All fields are required.", parent=self)
            return
        elif db.student_exist(roll_no):
            messagebox.showerror("Error", "Student with the same roll number already exists.", parent=self)
            return

        if db.add_student(roll_no, student_name, std_father_name, institution, level, year, contact_no, mail, address,):
            messagebox.showinfo("Success", "Student added successfully.", parent=self)
            # clears the entries after successful addition
            self.roll_entry.delete(0, "end")
            self.name_entry.delete(0, "end")
            self.father_entry.delete(0, "end")
            self.institution_entry.delete(0, "end")
            self.level_entry.delete(0, "end")
            self.year_entry.delete(0, "end")
            self.contact_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.address_entry.delete(0, "end")
        else:
            messagebox.showerror("Error", "Failed to add student check the logs.", parent=self) 

class GetStudent(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("TopLevel - Get Student")
        self.geometry("1200x500")
        self.resizable(False, False)
        self.configure(fg_color=bg)

        get_icon = ImageTk.PhotoImage(Image.open(get_std_icon_path).resize((60, 60)), Image.LANCZOS)

        title_label = ctk.CTkLabel(
            self,
            image=get_icon,
            compound="top",
            text="Get Student Info",
            font=("helvetica", 22, "bold"),
            text_color=text_fg
        )
        title_label.pack(fill="x", side="top", pady=(10, 0))

        sub_title_label = ctk.CTkLabel(
            self,
            text="Search for a Student in the Database by Roll Number",
            font=("Helvetica", 12),
            text_color="grey"
        )
        sub_title_label.pack(side="top", fill="x",pady=(0, 5))

        student_search_frame = ctk.CTkFrame(self, fg_color=bg)
        student_search_frame.pack(padx=30, pady=10, ipadx=20)

        self.roll_no_entry = ctk.CTkEntry(student_search_frame, placeholder_text="Enter roll number...", width=300)
        self.roll_no_entry.pack(side="right", padx=5, pady=5)

        search_btn = ctk.CTkButton(
            student_search_frame,
            text="Search",
            fg_color=btn_active,
            command=self.show_student_info,
            hover_color=btn_hvr
        )
        search_btn.pack(side="right", padx=5, pady=5)

        self.main_frame = ctk.CTkFrame(master=self, fg_color=bg, border_width=2, border_color=btn_active)
        self.main_frame.pack(fill="both", expand=True, padx=5, pady=5)

    def show_student_info(self):
        roll_no = self.roll_no_entry.get()
        if not roll_no:
            messagebox.showerror("Error", "Please enter a valid roll number.", parent=self)
            return
        if not roll_no.isdigit():
            messagebox.showerror("Error", "Roll number should be a number.", parent=self)
            return
        if roll_no == 0:
            messagebox.showerror("Error", "Roll number should not be zero.", parent=self)
            return
        
        # Fetch student data from database based on roll number
        student_data = db.get_student(roll_no)

        if student_data:
            self.name = student_data['name']
            self.father_name = student_data['father_name']
            self.institution = student_data['institution']
            self.level = student_data['level']
            self.year = student_data['year']
            self.contact_number = student_data['contact_no']
            self.email = student_data['mail']
            self.address = student_data['address']

        else:
            messagebox.showerror("Error", "No student found with the given roll number.", parent=self)
            return

        # destroy previous widgets in the frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # get student form frame 
        student_form_frame = ctk.CTkFrame(self.main_frame, fg_color=bg)
        student_form_frame.pack(padx=30, pady=10, ipadx=20)

        # roll number
        roll_label = ctk.CTkLabel(student_form_frame, text=f"Roll Number: {roll_no}", anchor="w", font=("Helvetica", 15, "bold"), text_color=text_fg)
        roll_label.grid(row=0, column=0, padx=5, pady=10)
        
        # student name
        name_label = ctk.CTkLabel(student_form_frame, text=f"Name: {self.name}", anchor="w", font=("Helvetica", 15, "bold"), text_color=text_fg)
        name_label.grid(row=1, column=0, padx=5, pady=10) 

        # father name
        father_label = ctk.CTkLabel(student_form_frame, text=f"Father's Name: {self.father_name}", anchor="w", font=("Helvetica", 15, "bold"), text_color=text_fg)
        father_label.grid(row=2, column=0, padx=5, pady=10)

        # institution name
        institution_label = ctk.CTkLabel(student_form_frame, text=f"Institution: {self.institution}", anchor="w", font=("Helvetica", 15, "bold"), text_color=text_fg)
        institution_label.grid(row=3, column=0, padx=5, pady=10)

        # level
        level_label = ctk.CTkLabel(student_form_frame, text=f"Level: {self.level}", anchor="w", font=("Helvetica", 15, "bold"), text_color=text_fg)
        level_label.grid(row=4, column=0, padx=5, pady=10)

        # year
        year_label = ctk.CTkLabel(student_form_frame, text=f"Year: {self.year}", anchor="w", font=("Helvetica", 15, "bold"), text_color=text_fg)
        year_label.grid(row=0, column=2, padx=(65, 5), pady=10)

        # contact number
        contact_label = ctk.CTkLabel(student_form_frame, text=f"Contact Number: {self.contact_number}", anchor="w", font=("Helvetica", 15, "bold"), text_color=text_fg)
        contact_label.grid(row=1, column=2, padx=(65, 5), pady=10)
        
        # email adddress
        email_label = ctk.CTkLabel(student_form_frame, text=f"Email Address: {self.email}", anchor="w", font=("Helvetica", 15, "bold"), text_color=text_fg)
        email_label.grid(row=2, column=2, padx=(65, 5), pady=10)

        # physical address
        address_label = ctk.CTkLabel(student_form_frame, text=f"Physical Address: {self.address}", anchor="w", font=("Helvetica", 15, "bold"), text_color=text_fg)
        address_label.grid(row=3, column=2, padx=(65, 5), pady=10)

        self.roll_no_entry.delete(0, "end")


class DeleteStudent(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("TopLevel - Delete Student")
        self.geometry("700x300")
        self.configure(fg_color=bg)
        self.resizable(False, False)

        del_icon = ImageTk.PhotoImage(Image.open(delete_icon_path).resize((60, 60)), Image.LANCZOS)

        title_label = ctk.CTkLabel(
            self,
            image=del_icon,
            compound="top",
            text="Delete Student",
            font=("helvetica", 22, "bold"),
            text_color=text_fg
        )
        title_label.pack(fill="x", side="top", pady=(10, 0))

        sub_title_label = ctk.CTkLabel(
            self,
            text="Delete a Student from the Database by Roll Number",
            font=("Helvetica", 12),
            text_color="grey"
        )
        sub_title_label.pack(side="top", fill="x", pady=(0, 5))

        student_search_frame = ctk.CTkFrame(self, fg_color=bg)
        student_search_frame.pack(padx=30, pady=10, ipadx=20)

        self.roll_no_entry = ctk.CTkEntry(student_search_frame, placeholder_text="Enter roll number...", width=300, corner_radius=5, fg_color=fg, border_color=btn_active)
        self.roll_no_entry.pack(side="right", padx=5, pady=5)

        del_btn = ctk.CTkButton(
            student_search_frame,
            text="Delete",
            fg_color=btn_active,
            command=self.delete_student,
            hover_color=btn_hvr
        )
        del_btn.pack(side="right", padx=5, pady=5)

    def delete_student(self):
        roll_no = self.roll_no_entry.get()
        if not roll_no:
            messagebox.showerror("Error", "Please enter a valid roll number.", parent=self)
            return
        if not roll_no.isdigit():
            messagebox.showerror("Error", "Roll number should be a number.", parent=self)
            return
        if roll_no == 0:
            messagebox.showerror("Error", "Roll number should not be zero.", parent=self)
            return

        # Delete student data from database based on roll number
        student = db.get_student(roll_no)
        if student:
            message = f"""
            Student found with\n
              Name: {student["name"]}\n
              Father name: {student["father_name"]}\n
              Institution: {student["institution"]}\n 
            Do you want to delete?
            """
            confirmed = messagebox.askyesno("Student found!", message, parent=self)
            if confirmed:
                if db.delete_student(roll_no):
                    messagebox.showinfo("Success", "Student deleted successfully.", parent=self)
                    self.roll_no_entry.delete(0, "end")
            else:
                return
        else:
            messagebox.showerror("Error", "Failed to delete student. Please check the roll number and try again.", parent=self)
