import customtkinter as ctk
import CTkTable as ctkt

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

class GetResult():
    def __init__(self, result_frame, roll_no_entry):

        for widget in result_frame.winfo_children():
            widget.destroy()

        roll_no = roll_no_entry.get()
        
        if not roll_no.isdigit():
            messagebox.show_error(title="Error", message="Invalid Roll Number!")
            return

        result = db.get_results_4_cs_ssc(roll_no)   
        if result:
            self.cs_ssc(result, result_frame)
        else:
            result = db.get_results_4_pm_ssc(roll_no)
            if result:
                self.pm_ssc(result, result_frame)
            else:
                result = db.get_results_4_cs_hssc(roll_no)
                if result:
                    self.cs_hssc(result, result_frame)
                else:
                    result = db.get_results_4_pm_hssc(roll_no)
                    if result:
                        self.pm_hssc(result, result_frame)
                    else:
                        messagebox.show_error(title="Error", message="No results found for this roll number.")

    def cs_ssc(self, result, result_frame):
        name = result["name"]
        father_name = result["father_name"]
        institution = result["institution"]
        exam_name = result["exam_name"]
        math = int(result["math"])
        physics = int(result["physics"])
        chemistry = int(result["chemistry"])
        computer = int(result["computer"])
        pak_studies = int(result["pak_studies"])
        islamiyat = int(result["islamiyat"])
        urdu = int(result["urdu"])
        english = int(result["english"])

        title = ctk.CTkLabel(
            result_frame,
            text=f"Result for SSC {exam_name} Computer Science",
            font=("Helvetica", -22, "bold"),
            fg_color=bg,
            text_color=text_fg
        )
        title.pack(pady=5, fill="x")

        marks1 = [math, physics, chemistry, computer, urdu, english]
        marks2 = [pak_studies, islamiyat]
        obt_marks = sum(marks1) + sum(marks2)

        if (math > 27 and physics > 27 and chemistry > 27 and computer > 27 and english > 27 and urdu > 27) and (pak_studies > 18 and islamiyat > 18):
            remarks = f"Pass with {obt_marks} marks"
        else:
            remarks = "Failed"

        ctk.CTkLabel(
            result_frame, 
            text=f"Name: {name.capitalize()}\nFather: {father_name.capitalize()}\nInstitution: {institution.capitalize()}\nResult: {remarks}",
            font=("Helvetica", -14),
            fg_color=bg,
            justify="left",
            anchor="w",
            text_color=text_fg
        ).pack(fill="x", pady=10, padx=10)

        marks_data = [
            ["Subjects", "Marks", "Grade", "GPA"],
            ["Math", math, self.get_grade(math, 75), self.get_gpa(math, 75)],
            ["Physics", physics, self.get_grade(physics, 75), self.get_gpa(physics, 75)],
            ["Chemistry", chemistry, self.get_grade(chemistry, 75), self.get_gpa(chemistry, 75)],
            ["Computer", computer, self.get_grade(computer, 75), self.get_gpa(computer, 75)],
            ["Pak Studies", pak_studies, self.get_grade(pak_studies, 50), self.get_gpa(pak_studies, 50)],
            ["Islamiyat", islamiyat, self.get_grade(islamiyat, 50), self.get_gpa(islamiyat, 50)],
            ["Urdu", urdu, self.get_grade(urdu, 75), self.get_gpa(urdu, 75)],
            ["English", english, self.get_grade(english, 75), self.get_gpa(english, 75)],
        ]
        
        t1 = ctk.CTkFrame(result_frame, fg_color=bg)
        t1.pack(fill="x", padx=5, pady=10,)

        table = ctkt.CTkTable(master=t1, values=marks_data, colors=[fg, bg], header_color=btn_active, hover_color=btn_hvr)
        table.edit_row(0, text_color=text_fg_2, hover_color=btn_hvr)
        table.pack(expand=True)

        gpas = [self.get_gpa(m, 75) for m in marks1] + [self.get_gpa(m, 50) for m in marks2]

        marks_data = [
            ["Total Marks", "Obt Marks", "Grade", "CGPA"],
            [550, obt_marks, self.get_grade(obt_marks, 550), self.get_cgpa(gpas)],
        ]
        t2 = ctk.CTkFrame(result_frame, fg_color=bg)
        t2.pack(fill="x", padx=5, pady=10,)

        table = ctkt.CTkTable(master=t2, values=marks_data, colors=[fg, fg], header_color=btn_active, hover_color=btn_hvr)
        table.edit_row(0, text_color=text_fg_2, hover_color=btn_hvr)
        table.pack(expand=True)

    def pm_ssc(self, result, result_frame):
        name = result["name"]
        father_name = result["father_name"]
        institution = result["institution"]
        exam_name = result["exam_name"]
        math = int(result["math"])
        physics = int(result["physics"])
        chemistry = int(result["chemistry"])
        biology = int(result["biology"])
        pak_studies = int(result["pak_studies"])
        islamiyat = int(result["islamiyat"])
        urdu = int(result["urdu"])
        english = int(result["english"])

        title = ctk.CTkLabel(
            result_frame,
            text=f"Result for SSC {exam_name} Pre Medical",
            font=("Helvetica", -22, "bold"),
            fg_color=bg,
            text_color=text_fg
        )
        title.pack(pady=5, fill="x")

        marks1 = [math, physics, chemistry, biology, urdu, english]
        marks2 = [pak_studies, islamiyat]
        obt_marks = sum(marks1) + sum(marks2)

        if (math > 27 and physics > 27 and chemistry > 27 and biology > 27 and english > 27 and urdu > 27) and (pak_studies > 18 and islamiyat > 18):
            remarks = f"Pass with {obt_marks} marks"
        else:
            remarks = "Failed"

        ctk.CTkLabel(
            result_frame, 
            text=f"Name: {name.capitalize()}\nFather: {father_name.capitalize()}\nInstitution: {institution.capitalize()}\nResult: {remarks}",
            font=("Helvetica", -14),
            fg_color=bg,
            justify="left",
            anchor="w",
            text_color=text_fg
        ).pack(fill="x", pady=10, padx=10)

        marks_data = [
            ["Subjects", "Marks", "Grade", "GPA"],
            ["Math", math, self.get_grade(math, 75), self.get_gpa(math, 75)],
            ["Physics", physics, self.get_grade(physics, 75), self.get_gpa(physics, 75)],
            ["Chemistry", chemistry, self.get_grade(chemistry, 75), self.get_gpa(chemistry, 75)],
            ["Biology", biology, self.get_grade(biology, 75), self.get_gpa(biology, 75)],
            ["Pak Studies", pak_studies, self.get_grade(pak_studies, 50), self.get_gpa(pak_studies, 50)],
            ["Islamiyat", islamiyat, self.get_grade(islamiyat, 50), self.get_gpa(islamiyat, 50)],
            ["Urdu", urdu, self.get_grade(urdu, 75), self.get_gpa(urdu, 75)],
            ["English", english, self.get_grade(english, 75), self.get_gpa(english, 75)],
        ]
        
        t1 = ctk.CTkFrame(result_frame, fg_color=bg)
        t1.pack(fill="x", padx=5, pady=10,)

        table = ctkt.CTkTable(master=t1, values=marks_data, colors=[fg, bg], header_color=btn_active, hover_color=btn_hvr)
        table.edit_row(0, text_color=text_fg_2, hover_color=btn_hvr)
        table.pack(expand=True)

        gpas = [self.get_gpa(m, 75) for m in marks1] + [self.get_gpa(m, 50) for m in marks2]

        marks_data = [
            ["Total Marks", "Obt Marks", "Grade", "CGPA"],
            [550, obt_marks, self.get_grade(obt_marks, 550), self.get_cgpa(gpas)],
        ]
        t2 = ctk.CTkFrame(result_frame, fg_color=bg)
        t2.pack(fill="x", padx=5, pady=10,)

        table = ctkt.CTkTable(master=t2, values=marks_data, colors=[fg, fg], header_color=btn_active, hover_color=btn_hvr)
        table.edit_row(0, text_color=text_fg_2, hover_color=btn_hvr)
        table.pack(expand=True)

    def cs_hssc(self, result, result_frame):
        name = result["name"]
        father_name = result["father_name"]
        institution = result["institution"]
        exam_name = result["exam_name"]
        math = result["math"]
        physics = result["physics"]
        computer = result["computer"]
        islamiyat_pak_studies = result["islamiyat/pak_studies"]
        urdu = result["urdu"]
        english = result["english"]

        title = ctk.CTkLabel(
            result_frame,
            text=f"Result for hSSC {exam_name} Computer Science",
            font=("Helvetica", -22, "bold"),
            fg_color=bg,
            text_color=text_fg
        )
        title.pack(pady=5, fill="x")

        marks1 = [math, physics, computer, urdu, english]
        marks2 = [islamiyat_pak_studies]
        obt_marks = sum(marks1) + sum(marks2)

        if math > 33 and physics > 33 and english > 33 and urdu > 33 and computer > 33 and islamiyat_pak_studies > 27:
            remarks = f"Pass with {obt_marks} marks"
        else:
            remarks = "Failed"

        ctk.CTkLabel(
            result_frame, 
            text=f"Name: {name.capitalize()}\nFather: {father_name.capitalize()}\nInstitution: {institution.capitalize()}\nResult: {remarks}",
            font=("Helvetica", -14),
            fg_color=bg,
            justify="left",
            anchor="w",
            text_color=text_fg
        ).pack(fill="x", pady=10, padx=10)

        marks_data = [
            ["Subjects", "Marks", "Grade", "GPA"],
            ["Math", math, self.get_grade(math, 100), self.get_gpa(math, 100)],
            ["Physics", physics, self.get_grade(physics, 100), self.get_gpa(physics, 100)],
            ["Computer Science", computer, self.get_grade(computer, 100), self.get_gpa(computer, 100)],
            ["Pak Studies/Islamiyat", islamiyat_pak_studies, self.get_grade(islamiyat_pak_studies, 50), self.get_gpa(islamiyat_pak_studies, 50)],
            ["Urdu", urdu, self.get_grade(urdu, 100), self.get_gpa(urdu, 100)],
            ["English", english, self.get_grade(english, 100), self.get_gpa(english, 100)],
        ]
        
        t1 = ctk.CTkFrame(result_frame, fg_color=bg)
        t1.pack(fill="x", padx=5, pady=10,)

        table = ctkt.CTkTable(master=t1, values=marks_data, colors=[fg, bg], header_color=btn_active, hover_color=btn_hvr)
        table.edit_row(0, text_color=text_fg_2, hover_color=btn_hvr)
        table.pack(expand=True)

        gpas = [self.get_gpa(m, 100) for m in marks1] + [self.get_gpa(m, 50) for m in marks2]

        marks_data = [
            ["Total Marks", "Obt Marks", "Grade", "CGPA"],
            [550, obt_marks, self.get_grade(obt_marks, 550), self.get_cgpa(gpas)],
        ]
        t2 = ctk.CTkFrame(result_frame, fg_color=bg)
        t2.pack(fill="x", padx=5, pady=10,)

        table = ctkt.CTkTable(master=t2, values=marks_data, colors=[fg, fg], header_color=btn_active, hover_color=btn_hvr)
        table.edit_row(0, text_color=text_fg_2, hover_color=btn_hvr)
        table.pack(expand=True)

    def pm_hssc(self, result, result_frame):
        name = result["name"]
        father_name = result["father_name"]
        institution = result["institution"]
        exam_name = result["exam_name"]
        chemistry = int(result["chemistry"])
        physics = int(result["physics"])
        biology = int(result["biology"])
        islamiyat_pak_studies = int(result["islamiyat/pak_studies"])
        urdu = int(result["urdu"])
        english = int(result["english"])

        title = ctk.CTkLabel(
            result_frame,
            text=f"Result for HSSC {exam_name} Pre Medical",
            font=("Helvetica", -22, "bold"),
            fg_color=bg,
            text_color=text_fg
        )
        title.pack(pady=5, fill="x")

        marks1 = [chemistry, physics, biology, urdu, english]
        marks2 = [islamiyat_pak_studies]
        obt_marks = sum(marks1) + sum(marks2)

        if chemistry > 33 and physics > 33 and english > 33 and urdu > 33 and biology > 33 and islamiyat_pak_studies > 27:
            remarks = f"Pass with {obt_marks} marks"
        else:
            remarks = "Failed"

        ctk.CTkLabel(
            result_frame, 
            text=f"Name: {name.capitalize()}\nFather: {father_name.capitalize()}\nInstitution: {institution.capitalize()}\nResult: {remarks}",
            font=("Helvetica", -14),
            fg_color=bg,
            justify="left",
            anchor="w",
            text_color=text_fg
        ).pack(fill="x", pady=10, padx=10)

        marks_data = [
            ["Subjects", "Marks", "Grade", "GPA"],
            ["Chemistry", chemistry, self.get_grade(chemistry, 100), self.get_gpa(chemistry, 100)],
            ["Physics", physics, self.get_grade(physics, 100), self.get_gpa(physics, 100)],
            ["Biology", biology, self.get_grade(biology, 100), self.get_gpa(biology, 100)],
            ["Pak Studies", islamiyat_pak_studies, self.get_grade(islamiyat_pak_studies, 50), self.get_gpa(islamiyat_pak_studies, 50)],
            ["Urdu", urdu, self.get_grade(urdu, 100), self.get_gpa(urdu, 100)],
            ["English", english, self.get_grade(english, 100), self.get_gpa(english, 100)],
        ]
        
        t1 = ctk.CTkFrame(result_frame, fg_color=bg)
        t1.pack(fill="x", padx=5, pady=10,)

        table = ctkt.CTkTable(master=t1, values=marks_data, colors=[fg, bg], header_color=btn_active, hover_color=btn_hvr)
        table.edit_row(0, text_color=text_fg_2, hover_color=btn_hvr)
        table.pack(expand=True)

        gpas = [self.get_gpa(m, 100) for m in marks1] + [self.get_gpa(m, 50) for m in marks2]

        marks_data = [
            ["Total Marks", "Obt Marks", "Grade", "CGPA"],
            [550, obt_marks, self.get_grade(obt_marks, 550), self.get_cgpa(gpas)],
        ]
        t2 = ctk.CTkFrame(result_frame, fg_color=bg)
        t2.pack(fill="x", padx=5, pady=10,)

        table = ctkt.CTkTable(master=t2, values=marks_data, colors=[fg, fg], header_color=btn_active, hover_color=btn_hvr)
        table.edit_row(0, text_color=text_fg_2, hover_color=btn_hvr)
        table.pack(expand=True)



    def get_grade(self, subject_marks, total_marks):
        percent = subject_marks/total_marks*100
        if percent >= 80:
            return "A+"
        elif percent >= 70:
            return "A"
        elif percent >= 60:
            return "B"
        elif percent >= 50:
            return "C"
        elif percent >= 45:
            return "D"
        elif percent >= 40:
            return "E"
        else:
            return "F"
        

    def get_gpa(self, subject_marks, total_marks):
        percent = subject_marks/total_marks*100
        if percent >= 90:
            return 4.0
        elif percent >= 80:
            return 3.5
        elif percent >= 70:
            return 3.0
        elif percent >= 60:
            return 2.5
        elif percent >= 50:
            return 2.0
        elif percent >= 40:
            return 1.0
        else:
            return 0.0
        
    def get_cgpa(self, gpas):
        if not gpas:
            return 0.0  

        total_gpa = sum(gpas)
        number_of_subjects = len(gpas)

        cgpa = total_gpa / number_of_subjects
        return round(cgpa, 2)