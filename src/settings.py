from customtkinter import CTkImage
from PIL import Image, ImageTk

import os

# Set the default path as "..\..\..\..\..\..\SERP-Manager"
base_path = r'/home/sbalghari/Documents/GitHub/SERP-Manager'

# Paths
current_role_path = os.path.join(base_path, "current_role.txt")
default_pdfs_path = os.path.join(base_path, "Papers")
cache_folder_path = os.path.join(base_path, "Cache")
acc_json_path = os.path.join(base_path, "json", "accounts.json")
current_role_path = os.path.join(base_path, "current_role.txt")
news_txt_path = os.path.join(base_path, "news.txt")
ssc1_json_path = os.path.join(base_path, "json", "ssc1_exams.json")
ssc2_json_path = os.path.join(base_path, "json", "ssc2_exams.json")
hssc1_json_path = os.path.join(base_path, "json", "hssc1_exams.json")
hssc2_json_path = os.path.join(base_path, "json", "hssc2_exams.json")

try:
    # Icons
    add_icon_path = os.path.join(base_path, "Icons", "add.png")
    refresh_icon_path = os.path.join(base_path, "Icons", "refresh.png")
    delete_icon_path = os.path.join(base_path, "Icons", "remove.png")
    exam_shortcut_icon_path = os.path.join(base_path, "Icons", "exam_shortcut.png")
    paper_shortcut_icon_path = os.path.join(base_path, "Icons", "paper_shortcut.png")
    result_shortcut_icon_path = os.path.join(base_path, "Icons", "result_shortcut.png")
    contact_us_icon_path = os.path.join(base_path, "Icons", "contact_us.png")
    add_exams_icon_path = os.path.join(base_path, "Icons", "add_exam.png")
    support_icon_path = os.path.join(base_path, "Icons", "support.png")
    news_icon_path = os.path.join(base_path, "Icons", "news.png")
    students_icon_path = os.path.join(base_path, "Icons", "student.png")
    teachers_icon_path = os.path.join(base_path, "Icons", "staff.png")
    right_arrow_icon_path = os.path.join(base_path, "Icons", "right_arrow.png")
    logout_icon_path = os.path.join(base_path, "Icons", "logout.png")
    edit_icon_path = os.path.join(base_path, "Icons", "edit.png")
    acc_icon_path = os.path.join(base_path, "Icons", "profile.png")
    search_icon_path = os.path.join(base_path, "Icons", "search.png")
    home_icon_path = os.path.join(base_path, "Icons", "home.png")
    side_icon_path = os.path.join(base_path, "Icons", "side_img.png")
    password_icon_path = os.path.join(base_path, "Icons", "password.png")
    name_icon_path = os.path.join(base_path, "Icons", "name.png")
    help_icon_path = os.path.join(base_path, "Icons", "help.png")
    shortcut_icon_path = os.path.join(base_path, "Icons", "shortcut.png")
    get_std_icon_path = os.path.join(base_path, "Icons", "get_std.png")
    edit_exam_icon_path = os.path.join(base_path, "Icons", "edit_paper.png")

    # Icons of Subjects(books)
    maths_icon_path = os.path.join(base_path, "Icons", "math.png")
    biology_icon_path = os.path.join(base_path, "Icons", "bio.png")
    english_icon_path = os.path.join(base_path, "Icons", "eng.png")
    urdu_icon_path = os.path.join(base_path, "Icons", "urdu.png")
    physics_icon_path = os.path.join(base_path, "Icons", "phy.png")
    chemistry_icon_path = os.path.join(base_path, "Icons", "chemistry.png")
    computer_icon_path = os.path.join(base_path, "Icons", "cs.png")
    islamiyat_icon_path = os.path.join(base_path, "Icons", "islamiyat.png")
    pk_std_icon_path = os.path.join(base_path, "Icons", "ps.png")

except FileNotFoundError as e:
    print(f"Error: {str(e)}")

# Converts and resize the PNG to ctkimage for buttons
refresh_pdfs_button_icon = CTkImage(Image.open(refresh_icon_path).resize((18, 18), Image.LANCZOS))
add_paper_button_icon = CTkImage(Image.open(add_exams_icon_path).resize((18, 18), Image.LANCZOS))
delete_paper_button_icon = CTkImage(Image.open(delete_icon_path).resize((18, 18), Image.LANCZOS))
contact_us_button_icon = CTkImage(Image.open(contact_us_icon_path).resize((18, 18), Image.LANCZOS))
add_exams_button_icon = CTkImage(Image.open(edit_exam_icon_path).resize((18, 18), Image.LANCZOS))
edit_button_icon = CTkImage(Image.open(edit_icon_path).resize((18, 18), Image.LANCZOS))
acc_button_icon = CTkImage(Image.open(acc_icon_path).resize((18, 18), Image.LANCZOS))
exam_button_icon = CTkImage(Image.open(exam_shortcut_icon_path).resize((18, 18), Image.LANCZOS))
result_button_icon = CTkImage(Image.open(result_shortcut_icon_path).resize((18, 18), Image.LANCZOS))
paper_button_icon = CTkImage(Image.open(paper_shortcut_icon_path).resize((18, 18), Image.LANCZOS))
search_button_icon = CTkImage(Image.open(search_icon_path).resize((18, 18), Image.LANCZOS))
home_button_icon = CTkImage(Image.open(home_icon_path).resize((18, 18), Image.LANCZOS))
students_button_icon = CTkImage(Image.open(students_icon_path).resize((18, 18), Image.LANCZOS))

# Icons
icons = {}

def setup_icons():
    global icons

    # Populate icons
    icons["phy_icon"] = ImageTk.PhotoImage(Image.open(physics_icon_path).resize((100, 100), Image.LANCZOS))
    icons["chem_icon"] = ImageTk.PhotoImage(Image.open(chemistry_icon_path).resize((100, 100), Image.LANCZOS))
    icons["bio_icon"] = ImageTk.PhotoImage(Image.open(biology_icon_path).resize((100, 100), Image.LANCZOS))
    icons["cs_icon"] = ImageTk.PhotoImage(Image.open(computer_icon_path).resize((100, 100), Image.LANCZOS))
    icons["isl_icon"] = ImageTk.PhotoImage(Image.open(islamiyat_icon_path).resize((100, 100), Image.LANCZOS))
    icons["math_icon"] = ImageTk.PhotoImage(Image.open(maths_icon_path).resize((100, 100), Image.LANCZOS))
    icons["urdu_icon"] = ImageTk.PhotoImage(Image.open(urdu_icon_path).resize((100, 100), Image.LANCZOS))
    icons["ps_icon"] = ImageTk.PhotoImage(Image.open(pk_std_icon_path).resize((100, 100), Image.LANCZOS))
    icons["eng_icon"] = ImageTk.PhotoImage(Image.open(english_icon_path).resize((100, 100), Image.LANCZOS))
    icons["default"] = ImageTk.PhotoImage(Image.open(english_icon_path).resize((100, 100), Image.LANCZOS))

    icons["news_icon"] = ImageTk.PhotoImage(Image.open(news_icon_path).resize((60, 60), Image.LANCZOS)) 

    icons["arrow_icon"] = ImageTk.PhotoImage(Image.open(right_arrow_icon_path).resize((20, 20), Image.LANCZOS)) 

    icons["shortcuts_icon"] = ImageTk.PhotoImage(Image.open(shortcut_icon_path).resize((60,60)), Image.LANCZOS) 

    icons["shortcut_1_icon"] = ImageTk.PhotoImage(Image.open(paper_shortcut_icon_path).resize((100, 100), Image.LANCZOS))                  
    icons["shortcut_2_icon"] = ImageTk.PhotoImage(Image.open(exam_shortcut_icon_path).resize((100, 100), Image.LANCZOS)) 
    icons["shortcut_3_icon"] = ImageTk.PhotoImage(Image.open(result_shortcut_icon_path).resize((100, 100), Image.LANCZOS))

    icons["help_icon"] = ImageTk.PhotoImage(Image.open(help_icon_path).resize((60,60)), Image.LANCZOS) 

    icons["role_1_icon"] = ImageTk.PhotoImage(Image.open(teachers_icon_path).resize((100, 100), Image.LANCZOS)) 
    icons["role_2_icon"] = ImageTk.PhotoImage(Image.open(students_icon_path).resize((100, 100), Image.LANCZOS)) 
    icons["support_icon"] = ImageTk.PhotoImage(Image.open(support_icon_path).resize((100, 100), Image.LANCZOS))

    icons["add_icon"] = ImageTk.PhotoImage(Image.open(add_exams_icon_path).resize((60, 60), Image.LANCZOS))
    icons["get_icon"] = ImageTk.PhotoImage(Image.open(get_std_icon_path).resize((60, 60), Image.LANCZOS))
    icons["del_icon"] = ImageTk.PhotoImage(Image.open(delete_icon_path).resize((60, 60), Image.LANCZOS))