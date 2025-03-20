from customtkinter import CTkImage
from PIL import Image, ImageTk

import os

base_path = os.path.expanduser("~/Documents/Github/SERP-Manager")

# Paths
current_role_path = os.path.join(base_path, "current_role.txt")
default_pdfs_path = os.path.join(base_path,"pdfs", "papers")
news_pdfs_path = os.path.join(base_path,"pdfs", "news")
cache_folder_path = os.path.join(base_path, "cache")
acc_json_path = os.path.join(base_path, "json", "accounts.json")
current_role_path = os.path.join(base_path, "current_role.txt")
news_txt_path = os.path.join(base_path, "news.txt")
ssc1_json_path = os.path.join(base_path, "json", "ssc1_exams.json")
ssc2_json_path = os.path.join(base_path, "json", "ssc2_exams.json")
hssc1_json_path = os.path.join(base_path, "json", "hssc1_exams.json")
hssc2_json_path = os.path.join(base_path, "json", "hssc2_exams.json")

try:
    # Icons
    add_icon_path = os.path.join(base_path, "icons", "add.png")
    refresh_icon_path = os.path.join(base_path, "icons", "refresh.png")
    delete_icon_path = os.path.join(base_path, "icons", "remove.png")
    exam_shortcut_icon_path = os.path.join(base_path, "icons", "exam_shortcut.png")
    paper_shortcut_icon_path = os.path.join(base_path, "icons", "paper_shortcut.png")
    result_shortcut_icon_path = os.path.join(base_path, "icons", "result_shortcut.png")
    contact_us_icon_path = os.path.join(base_path, "icons", "contact_us.png")
    add_exams_icon_path = os.path.join(base_path, "icons", "add_exam.png")
    support_icon_path = os.path.join(base_path, "icons", "support.png")
    news_icon_path = os.path.join(base_path, "icons", "news.png")
    students_icon_path = os.path.join(base_path, "icons", "student.png")
    teachers_icon_path = os.path.join(base_path, "icons", "staff.png")
    right_arrow_icon_path = os.path.join(base_path, "icons", "right_arrow.png")
    logout_icon_path = os.path.join(base_path, "icons", "logout.png")
    edit_icon_path = os.path.join(base_path, "icons", "edit.png")
    acc_icon_path = os.path.join(base_path, "icons", "profile.png")
    search_icon_path = os.path.join(base_path, "icons", "search.png")
    home_icon_path = os.path.join(base_path, "icons", "home.png")
    side_icon_path = os.path.join(base_path, "icons", "side_img.png")
    password_icon_path = os.path.join(base_path, "icons", "password.png")
    name_icon_path = os.path.join(base_path, "icons", "name.png")
    shortcut_icon_path = os.path.join(base_path, "icons", "shortcut.png")
    get_std_icon_path = os.path.join(base_path, "icons", "get_std.png")
    edit_exam_icon_path = os.path.join(base_path, "icons", "edit_paper.png")
    help_icon_path = os.path.join(base_path, "icons", "help.png")
    success_icon_path = os.path.join(base_path, "icons", "success.png")
    error_icon_path = os.path.join(base_path, "icons", "error.png")
    yes_no_icon_path = os.path.join(base_path, "icons", "yes_no.png")
    warn_icon_path = os.path.join(base_path, "icons", "warn.png")
    info_icon_path = os.path.join(base_path, "icons", "info.png")

    # Socials icons
    instagram_icon_path = os.path.join(base_path, "icons", "instagram.png")
    linkedin_icon_path = os.path.join(base_path, "icons", "linkedin.png")
    github_icon_path = os.path.join(base_path, "icons", "github.png")
    youtube_icon_path = os.path.join(base_path, "icons", "youtube.png")

    # Icons of Subjects(books) icons
    maths_icon_path = os.path.join(base_path, "icons", "math.png")
    biology_icon_path = os.path.join(base_path, "icons", "bio.png")
    english_icon_path = os.path.join(base_path, "icons", "eng.png")
    urdu_icon_path = os.path.join(base_path, "icons", "urdu.png")
    physics_icon_path = os.path.join(base_path, "icons", "phy.png")
    chemistry_icon_path = os.path.join(base_path, "icons", "chemistry.png")
    computer_icon_path = os.path.join(base_path, "icons", "cs.png")
    islamiyat_icon_path = os.path.join(base_path, "icons", "islamiyat.png")
    pk_std_icon_path = os.path.join(base_path, "icons", "ps.png")

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

    icons["shortcut_1_icon"] = ImageTk.PhotoImage(Image.open(paper_shortcut_icon_path).resize((80, 80), Image.LANCZOS))                  
    icons["shortcut_2_icon"] = ImageTk.PhotoImage(Image.open(exam_shortcut_icon_path).resize((80, 80), Image.LANCZOS)) 
    icons["shortcut_3_icon"] = ImageTk.PhotoImage(Image.open(result_shortcut_icon_path).resize((80, 80), Image.LANCZOS))
    icons["shortcut_4_icon"] = ImageTk.PhotoImage(Image.open(students_icon_path).resize((80, 80), Image.LANCZOS))

    icons["help_icon"] = ImageTk.PhotoImage(Image.open(help_icon_path).resize((60,60)), Image.LANCZOS) 

    icons["role_1_icon"] = ImageTk.PhotoImage(Image.open(teachers_icon_path).resize((100, 100), Image.LANCZOS)) 
    icons["role_2_icon"] = ImageTk.PhotoImage(Image.open(students_icon_path).resize((100, 100), Image.LANCZOS)) 
    icons["support_icon"] = ImageTk.PhotoImage(Image.open(support_icon_path).resize((100, 100), Image.LANCZOS))

    icons["add_icon"] = ImageTk.PhotoImage(Image.open(add_exams_icon_path).resize((60, 60), Image.LANCZOS))
    icons["get_icon"] = ImageTk.PhotoImage(Image.open(get_std_icon_path).resize((60, 60), Image.LANCZOS))
    icons["del_icon"] = ImageTk.PhotoImage(Image.open(delete_icon_path).resize((60, 60), Image.LANCZOS))

    icons["github"] = ImageTk.PhotoImage(Image.open(github_icon_path).resize((60, 60), Image.LANCZOS))
    icons["youtube"] = ImageTk.PhotoImage(Image.open(youtube_icon_path).resize((60, 60), Image.LANCZOS))
    icons["instagram"] = ImageTk.PhotoImage(Image.open(instagram_icon_path).resize((60, 60), Image.LANCZOS))
    icons["linkedin"] = ImageTk.PhotoImage(Image.open(linkedin_icon_path).resize((60, 60), Image.LANCZOS))
    