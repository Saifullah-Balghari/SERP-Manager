import customtkinter as ctk
from PIL import Image

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

    # Icons of Subjects
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
refresh_pdfs_button_icon = ctk.CTkImage(Image.open(refresh_icon_path).resize((18, 18), Image.LANCZOS))
add_paper_button_icon = ctk.CTkImage(Image.open(add_icon_path).resize((18, 18), Image.LANCZOS))
delete_paper_button_icon = ctk.CTkImage(Image.open(delete_icon_path).resize((18, 18), Image.LANCZOS))
contact_us_button_icon = ctk.CTkImage(Image.open(contact_us_icon_path).resize((18, 18), Image.LANCZOS))
add_exams_button_icon = ctk.CTkImage(Image.open(add_exams_icon_path).resize((18, 18), Image.LANCZOS))
edit_button_icon = ctk.CTkImage(Image.open(edit_icon_path).resize((18, 18), Image.LANCZOS))
acc_button_icon = ctk.CTkImage(Image.open(acc_icon_path).resize((18, 18), Image.LANCZOS))
exam_button_icon = ctk.CTkImage(Image.open(exam_shortcut_icon_path).resize((18, 18), Image.LANCZOS))
result_button_icon = ctk.CTkImage(Image.open(result_shortcut_icon_path).resize((18, 18), Image.LANCZOS))
paper_button_icon = ctk.CTkImage(Image.open(paper_shortcut_icon_path).resize((18, 18), Image.LANCZOS))